from flask import Flask, render_template, request, redirect, url_for
import json, os, uuid
from datetime import datetime

app = Flask(__name__)
DB_PATH = "db.json"

# ---------------- Base de données ----------------
def default_db():
    return {
        "emails": [],
        "year_goals": [],
        "month_goals": [],
        "weekly_tasks": [],
        "daily_tasks": []
    }

def load_db():
    if not os.path.exists(DB_PATH):
        save_db(default_db())
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------------- ROUTES ----------------

@app.route("/")
def home():
    db = load_db()
    return render_template("home.html", emails=db.get("emails", []))


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email", "").strip()
    if email:
        db = load_db()
        if email not in db["emails"]:
            db["emails"].append(email)
            save_db(db)
    return redirect(url_for("home"))


# --- Objectifs annuels ---
@app.route("/goals-year", methods=["GET", "POST"])
def goals_year():
    db = load_db()
    if request.method == "POST":
        content = request.form.get("content", "").strip()
        if content:
            db["year_goals"].append({
                "id": str(uuid.uuid4()),
                "content": content,
                "done": False
            })
            save_db(db)
        return redirect(url_for("goals_year"))
    return render_template("goals_year.html", goals=db.get("year_goals", []))


@app.route("/goals-year/toggle", methods=["POST"])
def goals_year_toggle():
    gid = request.form.get("id")
    db = load_db()
    for g in db["year_goals"]:
        if g["id"] == gid:
            g["done"] = not g.get("done", False)
    save_db(db)
    return redirect(url_for("goals_year"))


@app.route("/goals-year/delete", methods=["POST"])
def goals_year_delete():
    gid = request.form.get("id")
    db = load_db()
    db["year_goals"] = [g for g in db["year_goals"] if g["id"] != gid]
    save_db(db)
    return redirect(url_for("goals_year"))


# --- Objectifs mensuels ---
@app.route("/goals-month", methods=["GET", "POST"])
def goals_month():
    db = load_db()
    if request.method == "POST":
        content = request.form.get("content", "").strip()
        if content:
            db["month_goals"].append({
                "id": str(uuid.uuid4()),
                "content": content,
                "done": False
            })
            save_db(db)
        return redirect(url_for("goals_month"))
    return render_template("goals_month.html", goals=db.get("month_goals", []))


@app.route("/goals-month/toggle", methods=["POST"])
def goals_month_toggle():
    gid = request.form.get("id")
    db = load_db()
    for g in db["month_goals"]:
        if g["id"] == gid:
            g["done"] = not g.get("done", False)
    save_db(db)
    return redirect(url_for("goals_month"))


@app.route("/goals-month/delete", methods=["POST"])
def goals_month_delete():
    gid = request.form.get("id")
    db = load_db()
    db["month_goals"] = [g for g in db["month_goals"] if g["id"] != gid]
    save_db(db)
    return redirect(url_for("goals_month"))


# --- Tâches hebdomadaires ---
@app.route("/weekly", methods=["GET", "POST"])
def weekly():
    db = load_db()
    if request.method == "POST":
        content = request.form.get("content", "").strip()
        if content:
            db.setdefault("weekly_tasks", []).append({
                "id": str(uuid.uuid4()),
                "content": content,
                "done": False
            })
            save_db(db)
        return redirect(url_for("weekly"))
    return render_template("weekly.html", tasks=db.get("weekly_tasks", []))


@app.route("/weekly/toggle", methods=["POST"])
def weekly_toggle():
    tid = request.form.get("id")
    db = load_db()
    for t in db.get("weekly_tasks", []):
        if t["id"] == tid:
            t["done"] = not t.get("done", False)
    save_db(db)
    return redirect(url_for("weekly"))


@app.route("/weekly/delete", methods=["POST"])
def weekly_delete():
    tid = request.form.get("id")
    db = load_db()
    db["weekly_tasks"] = [t for t in db.get("weekly_tasks", []) if t["id"] != tid]
    save_db(db)
    return redirect(url_for("weekly"))


# --- Tâches quotidiennes ---
@app.route("/daily", methods=["GET", "POST"])
def daily():
    db = load_db()

    if "daily_tasks" not in db:
        db["daily_tasks"] = []
        save_db(db)

    if request.method == "POST":
        cat = request.form.get("categorie", "").strip()
        content = request.form.get("content", "").strip()
        if content and cat in ["Physique", "Spirituel", "Mental", "Responsabilité"]:
            db["daily_tasks"].append({
                "id": str(uuid.uuid4()),
                "categorie": cat,
                "content": content,
                "done": False,
                "completed_at": None
            })
            save_db(db)
        return redirect(url_for("daily"))

    # Organisation par catégorie
    categories = {
        "Physique": [],
        "Spirituel": [],
        "Mental": [],
        "Responsabilité": []
    }

    for t in db.get("daily_tasks", []):
        cat = t.get("categorie", "")
        if cat in categories:
            categories[cat].append(t)

    return render_template("daily.html", categories=categories)


@app.route("/daily/toggle", methods=["POST"])
def daily_toggle():
    tid = request.form.get("id")
    db = load_db()

    for t in db.get("daily_tasks", []):
        if t["id"] == tid:
            t["done"] = not t.get("done", False)
            t["completed_at"] = datetime.now().isoformat() if t["done"] else None
            break

    save_db(db)
    return redirect(url_for("daily"))


@app.route("/daily/delete", methods=["POST"])
def daily_delete():
    tid = request.form.get("id")
    db = load_db()
    db["daily_tasks"] = [t for t in db.get("daily_tasks", []) if t["id"] != tid]
    save_db(db)
    return redirect(url_for("daily"))


# --- Statistiques de productivité ---
@app.route("/productivity")
def productivity():
    db = load_db()

    stats = {
        "daily": {
            "total": len(db.get("daily_tasks", [])),
            "done": sum(1 for t in db.get("daily_tasks", []) if t["done"])
        },
        "weekly": {
            "total": len(db.get("weekly_tasks", [])),
            "done": sum(1 for t in db.get("weekly_tasks", []) if t["done"])
        },
        "monthly": {
            "total": len(db.get("month_goals", [])),
            "done": sum(1 for t in db.get("month_goals", []) if t["done"])
        },
        "yearly": {
            "total": len(db.get("year_goals", [])),
            "done": sum(1 for t in db.get("year_goals", []) if t["done"])
        },
    }

    return render_template("productivity.html", stats=stats)


# --- Pages simples ---
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/start")
def start():
    return render_template("start.html")


# --- Lancement ---
if __name__ == "__main__":
    app.run(debug=True)
