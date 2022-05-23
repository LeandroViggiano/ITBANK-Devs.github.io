/*Esto se encarga de que al hacer click en una opcion, se desplieguen mas opciones */
let hideText_btn = document.getElementById("Tusdatos");
let hideText = document.getElementById("hideTusdatos");

hideText_btn.addEventListener("click", function (event) {
    event.preventDefault(); /*Evita acciones por default de las etiquetas */
    toggleText(hideText)
});
/*------------------------------------------------- */
let hideText_btn1 = document.getElementById("Seguridad");
let hideText1 = document.getElementById("hideSeguridad");

hideText_btn1.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideText1)
}); 
/*------------------------------------------------- */
let hideText_btn2 = document.getElementById("Tustarjetas");
let hideText2 = document.getElementById("hideTustarjetas");

hideText_btn2.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideText2)
}); 
/*------------------------------------------------- */
let hideText_btn3 = document.getElementById("Direcciones");
let hideText3 = document.getElementById("hideDirecciones");

hideText_btn3.addEventListener("click", function (event) {
   event.preventDefault();
   toggleText(hideText3)
}); 
/*------------------------------------------------- */
let hideText_btn4 = document.getElementById("Privacidad");
let hideText4 = document.getElementById("hidePrivacidad");

hideText_btn4.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideText4)
}); 

/*------------------------------------------------- */
let hideText_btn5 = document.getElementById("Comunicaciones");
let hideText5 = document.getElementById("hideComunicaciones");

hideText_btn5.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideText5)
}); 
/*------------------------------------------------- */
let hideText_btn6 = document.getElementById("Subscripciones");
let hideText6 = document.getElementById("hideSubscripciones");

hideText_btn6.addEventListener("click", function (event) {
    event.preventDefault();
    toggleText(hideText6)
}); 
/*------------------------------------------------- */
function toggleText(element) {
    element.classList.toggle("show");
}