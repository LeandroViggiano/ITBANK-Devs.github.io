const hamburger = document.getElementById("menu");
const panel = document.querySelector(".izquierda");

hamburger.addEventListener("click", (e) => {
    panel.classList.toggle("block")
    hamburger.classList.toggle("block")
})

/* APP MOBIL */

if(navigator.userAgent.match(/android/i)){
    const alerta = document.querySelector(".mensaje-app").style.setProperty("display", "block")
    const mensaje = document.querySelector(".app").textContent= "¡Descargá nuestra app en la Play Store!"
} 

if(navigator.userAgent.match(/iphone | ipad/i)) {
    const alerta = document.querySelector(".mensaje-app").style.setProperty("display", "block")
    const mensaje = document.querySelector(".app").textContent= "¡Descargá nuestra app en la App Store!"
}

/* CAROUSEL */
const imagen = document.getElementById("imagen1");

document.addEventListener("click", (e) => {
    if(e.target.matches("#izquierda")){
        if(imagen.getAttribute("src") === "¿TODAVIA NO PEDISTE LA NUEVA TARJETA ITABANK GOLD.png"){
            imagen.setAttribute("src", "banner2.png")
        }else if(imagen.getAttribute("src") === "banner2.png"){
            imagen.setAttribute("src", "¿TODAVIA NO PEDISTE LA NUEVA TARJETA ITABANK GOLD.png")
        }
    }
    
    if(e.target.matches("#derecha")){
        if(imagen.getAttribute("src") === "¿TODAVIA NO PEDISTE LA NUEVA TARJETA ITABANK GOLD.png"){
            imagen.setAttribute("src", "banner2.png")
        }else if(imagen.getAttribute("src") === "banner2.png"){
            imagen.setAttribute("src", "¿TODAVIA NO PEDISTE LA NUEVA TARJETA ITABANK GOLD.png")
        }
    }
})