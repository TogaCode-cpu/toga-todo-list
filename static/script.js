console.log("JS chargé !");

// Confirmation avant suppression
document.querySelectorAll("form[action$='/delete'] button").forEach(btn=>{
    btn.addEventListener("click", function(e){
        if(!confirm("Voulez-vous vraiment supprimer cette tâche ?")){
            e.preventDefault();
        }
    });
});

// Visual feedback pour toggle done
document.querySelectorAll("form[action$='/toggle'] button").forEach(btn=>{
    btn.addEventListener("click", function(){
        const li=btn.closest("li");
        li.classList.toggle("list-group-item-success");
    });
});
