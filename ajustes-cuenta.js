let Tusdatos = document.getElementById("Tusdatos");
let hideTusdatos = document.getElementById("hideTusdatos");

/* MENU HAMBURGUESA */
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

Tusdatos.addEventListener("click", function (event) {
    event.preventDefault(); /*Evita acciones por default de las etiquetas */
    toggleText(hideTusdatos)/*Esto se encarga de que al hacer click en una opcion, se desplieguen mas opciones */
    if(hideComunicaciones.classList.contains("show")){
        toggleText(hideComunicaciones);
    }
    if(hideSubscripciones.classList.contains("show")){
        toggleText(hideSubscripciones);
    }
    if(hidePrivacidad.classList.contains("show")){
        toggleText(hidePrivacidad);
    }
    if(hideTustarjetas.classList.contains("show")){
        toggleText(hideTustarjetas);
    }
    if(hideSeguridad.classList.contains("show")){
        toggleText(hideSeguridad);
    }
    if(hideDirecciones.classList.contains("show")){
        toggleText(hideDirecciones);
    }
});
/*------------------------------------------------- */
let Seguridad = document.getElementById("Seguridad");
let hideSeguridad = document.getElementById("hideSeguridad");

Seguridad.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideSeguridad);
    if(hideComunicaciones.classList.contains("show")){
        toggleText(hideComunicaciones);
    }
    if(hideSubscripciones.classList.contains("show")){
        toggleText(hideSubscripciones);
    }
    if(hidePrivacidad.classList.contains("show")){
        toggleText(hidePrivacidad);
    }
    if(hideTustarjetas.classList.contains("show")){
        toggleText(hideTustarjetas);
    }
    if(hideDirecciones.classList.contains("show")){
        toggleText(hideDirecciones);
    }
    if(hideTusdatos.classList.contains("show")){
        toggleText(hideTusdatos);
    }
}); 
/*------------------------------------------------- */
let Tustarjetas = document.getElementById("Tustarjetas");
let hideTustarjetas = document.getElementById("hideTustarjetas");

Tustarjetas.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideTustarjetas);
    if(hideComunicaciones.classList.contains("show")){
        toggleText(hideComunicaciones);
    }
    if(hideSubscripciones.classList.contains("show")){
        toggleText(hideSubscripciones);
    }
    if(hidePrivacidad.classList.contains("show")){
        toggleText(hidePrivacidad);
    }
    if(hideDirecciones.classList.contains("show")){
        toggleText(hideDirecciones);
    }
    if(hideSeguridad.classList.contains("show")){
        toggleText(hideSeguridad);
    }
    if(hideTusdatos.classList.contains("show")){
        toggleText(hideTusdatos);
    }
}); 
/*------------------------------------------------- */
let Direcciones = document.getElementById("Direcciones");
let hideDirecciones = document.getElementById("hideDirecciones");

Direcciones.addEventListener("click", function (event) {
   event.preventDefault();
   toggleText(hideDirecciones);
   if(hideComunicaciones.classList.contains("show")){
    toggleText(hideComunicaciones);
}
if(hideSubscripciones.classList.contains("show")){
    toggleText(hideSubscripciones);
}
if(hidePrivacidad.classList.contains("show")){
    toggleText(hidePrivacidad);
}
if(hideTustarjetas.classList.contains("show")){
    toggleText(hideTustarjetas);
}
if(hideSeguridad.classList.contains("show")){
    toggleText(hideSeguridad);
}
if(hideTusdatos.classList.contains("show")){
    toggleText(hideTusdatos);
}
}); 
/*------------------------------------------------- */
let Privacidad = document.getElementById("Privacidad");
let hidePrivacidad = document.getElementById("hidePrivacidad");

Privacidad.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hidePrivacidad);
    if(hideComunicaciones.classList.contains("show")){
        toggleText(hideComunicaciones);
    }
    if(hideSubscripciones.classList.contains("show")){
        toggleText(hideSubscripciones);
    }
    if(hideDirecciones.classList.contains("show")){
        toggleText(hideDirecciones);
    }
    if(hideTustarjetas.classList.contains("show")){
        toggleText(hideTustarjetas);
    }
    if(hideSeguridad.classList.contains("show")){
        toggleText(hideSeguridad);
    }
    if(hideTusdatos.classList.contains("show")){
        toggleText(hideTusdatos);
    }

}); 

/*------------------------------------------------- */
let Comunicaciones = document.getElementById("Comunicaciones");
let hideComunicaciones = document.getElementById("hideComunicaciones");

Comunicaciones.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideComunicaciones);
    if(hideSubscripciones.classList.contains("show")){
        toggleText(hideSubscripciones);
    }
    if(hidePrivacidad.classList.contains("show")){
        toggleText(hidePrivacidad);
    }
    if(hideDirecciones.classList.contains("show")){
        toggleText(hideDirecciones);
    }
    if(hideTustarjetas.classList.contains("show")){
        toggleText(hideTustarjetas);
    }
    if(hideSeguridad.classList.contains("show")){
        toggleText(hideSeguridad);
    }
    if(hideTusdatos.classList.contains("show")){
        toggleText(hideTusdatos);
    }

}); 
/*------------------------------------------------- */
let Subscripciones = document.getElementById("Subscripciones");
let hideSubscripciones = document.getElementById("hideSubscripciones");

Subscripciones.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideSubscripciones);
    if(hideComunicaciones.classList.contains("show")){
        toggleText(hideComunicaciones);
    }
    if(hidePrivacidad.classList.contains("show")){
        toggleText(hidePrivacidad);
    }
    if(hideDirecciones.classList.contains("show")){
        toggleText(hideDirecciones);
    }
    if(hideTustarjetas.classList.contains("show")){
        toggleText(hideTustarjetas);
    }
    if(hideSeguridad.classList.contains("show")){
        toggleText(hideSeguridad);
    }
    if(hideTusdatos.classList.contains("show")){
        toggleText(hideTusdatos);
    }
}); 
/*------------------------------------------------- */
function toggleText(element) {
    element.classList.toggle("show");
}