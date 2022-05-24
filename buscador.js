/* BUSCADOR */

document.addEventListener("keyup", (e) => {
    if(e.target.matches("#buscador")){

        document.querySelectorAll(".opcion-buscador").forEach(opcion =>{

            opcion.textContent.toLowerCase().includes(e.target.value.toLowerCase())
            ?opcion.classList.add("oculto")
            :opcion.classList.remove("oculto")


            if(document.getElementById("buscador").value.length === 0){
                opcion.classList.remove("oculto")
            }
        })


    }
})
