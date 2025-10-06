# Toga List 📝

**Toga List** est une application web de type **To-Do List** qui permet de gérer tes objectifs et tes tâches à différentes échelles de temps : annuelle, mensuelle, hebdomadaire et quotidienne. Elle inclut également un suivi de la productivité grâce à des graphiques interactifs.

---

## Fonctionnalités principales

1. **Page d'accueil**  
   - Présentation de l'application.  
   - Formulaire d'inscription à la newsletter (optionnel).

2. **Objectifs annuels (`/goals-year`)**  
   - Ajouter, supprimer et marquer comme terminé les objectifs de l'année.  

3. **Objectifs mensuels (`/goals-month`)**  
   - Ajouter, supprimer et marquer comme terminé les objectifs du mois.  

4. **Tâches hebdomadaires (`/weekly`)**  
   - Gestion des tâches répétitives chaque semaine.  

5. **Tâches quotidiennes (`/daily`)**  
   - Gestion des tâches journalières, organisées en 4 catégories :
     - **Physique** (Physical Win)
     - **Spirituel** (Spiritual Win)
     - **Mental** (Mental Win)
     - **Responsabilité** (Accountability Win)  
   - Ajouter, supprimer et marquer comme terminé les tâches.  
   - Les tâches terminées affichent un style et un badge distinct.

6. **Productivité (`/productivity`)**  
   - Graphique interactif montrant le nombre de tâches terminées : quotidien, hebdomadaire, mensuel et annuel.

---

## Installation

1. **Cloner le dépôt :**
```bash
git clone # Toga List 📝

**Toga List** est une application web de type **To-Do List** qui permet de gérer tes objectifs et tes tâches à différentes échelles de temps : annuelle, mensuelle, hebdomadaire et quotidienne. Elle inclut également un suivi de la productivité grâce à des graphiques interactifs.

---

## Fonctionnalités principales

1. **Page d'accueil**  
   - Présentation de l'application.  
   - Formulaire d'inscription à la newsletter (optionnel).

2. **Objectifs annuels (`/goals-year`)**  
   - Ajouter, supprimer et marquer comme terminé les objectifs de l'année.  

3. **Objectifs mensuels (`/goals-month`)**  
   - Ajouter, supprimer et marquer comme terminé les objectifs du mois.  

4. **Tâches hebdomadaires (`/weekly`)**  
   - Gestion des tâches répétitives chaque semaine.  

5. **Tâches quotidiennes (`/daily`)**  
   - Gestion des tâches journalières, organisées en 4 catégories :
     - **Physique** (Physical Win)
     - **Spirituel** (Spiritual Win)
     - **Mental** (Mental Win)
     - **Responsabilité** (Accountability Win)  
   - Ajouter, supprimer et marquer comme terminé les tâches.  
   - Les tâches terminées affichent un style et un badge distinct.

6. **Productivité (`/productivity`)**  
   - Graphique interactif montrant le nombre de tâches terminées : quotidien, hebdomadaire, mensuel et annuel.

---

## Installation

1. **Cloner le dépôt :**
```bash
git clone https://github.com/TogaCode-cpu/toga-list.git
cd toga-list

cd toga-list
2. ** Créer un environnement virtuel (optionnel mais recommandé) :**
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

3. **Installer les dépendances :**
pip install flask

4.  ** Lancer l'application :**
python app.py

5. **Ouvrir dans le navigateur :**
http://127.0.0.1:5000

## Structure du projet

toga-list/
│
├─ app.py                 # Application Flask
├─ db.json                # Base de données JSON
├─ templates/             # Templates HTML
│   ├─ base.html
│   ├─ home.html
│   ├─ goals_year.html
│   ├─ goals_month.html
│   ├─ weekly.html
│   ├─ daily.html
│   └─ productivity.html
    
│
├─ static/
│   ├─ style.css          # Styles CSS globalisés
│   └─ script.js          # Scripts JS interactifs
│
└─ README.md

## Technologies utilisées
Frontend : HTML, CSS, Bootstrap 5, JS, Chart.js
Backend : Python, Flask
Base de données : JSON local (db.json)


