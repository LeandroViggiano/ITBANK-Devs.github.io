/* DOM */

/*document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const fondo = document.querySelector(".fondo-dom").style.setProperty("display", "none")    
    }, 4000);
    
})*/

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

/* AÑADIR NUEVA TARJETA */

const añadirTarjeta = document.querySelector(".nueva_tarjeta")

document.addEventListener("click", (e) => {

    // Boton +
    if(e.target.matches(".nueva_tarjeta i")){
        document.querySelector(".crearTarjetas").style.display = "flex"

        document.querySelector(".derecha").style.opacity = ".3"
    }

    // Cerrar pestaña X
    if(e.target.matches(".cerrar i")){
        document.querySelector(".crearTarjetas").style.display = "none"

        document.querySelector(".derecha").style.opacity = "1"
    }

   
})

const formularioTarjeta = document.getElementById("formularioTarjeta")
const valoresNumero = document.querySelector(".numero"),
valoresNombre = document.querySelector(".nombreUsuario")

formularioTarjeta.addEventListener("submit", (e) => {
    e.preventDefault();

     /* // crear elementos y insertarlos en el html
        const divTarjeta = document.createElement("div");
        divTarjeta.setAttribute("class","tarjeta")

        const imagen = document.createElement("img")
        imagen.setAttribute("src", "tarjeta1.png")

        const divNuevaTarjeta=document.querySelector(".nueva_tarjeta")
        divNuevaTarjeta.insertAdjacentElement("beforebegin" ,divTarjeta)
        divTarjeta.appendChild(imagen)
        */

        // cerrar ventana
        document.querySelector(".crearTarjetas").style.display = "none"

        document.querySelector(".derecha").style.opacity = "1"

        // Crear una tarjeta: todos los elementos

        /* Div padre */
        const divPadre = document.createElement("div");
        divPadre.setAttribute("class", "tarjeta")

        const divNuevaTarjeta=document.querySelector(".nueva_tarjeta")
        divNuevaTarjeta.insertAdjacentElement("beforebegin" ,divPadre)
        /* Divs hijos */

        // Primer div: Logo
        const logo = document.createElement("div")
        logo.setAttribute("class","logo")
        divPadre.appendChild(logo)

        const conjuntoLogo = document.createElement("div");
        conjuntoLogo.setAttribute("class","conjunto-logo");
        logo.appendChild(conjuntoLogo)

        const chip = document.createElement("img")
        chip.setAttribute("src","chip.png")
        conjuntoLogo.appendChild(chip)

        const pItbank = document.createElement("p")
        pItbank.textContent = "ITBANK"
        conjuntoLogo.appendChild(pItbank)


        // Segundo div: Numero Tarjeta

        const numeroTarjeta = document.createElement("div")
        numeroTarjeta.setAttribute("class","numeroTarjeta")
        divPadre.appendChild(numeroTarjeta)

        const resultadoNumero = document.createElement("p")
        resultadoNumero.setAttribute("class","numero")
        resultadoNumero.textContent = valoresNumero.value
        numeroTarjeta.appendChild(resultadoNumero)

        // Tercer div: nombre y visa

        const conjuntoNombreVisa = document.createElement("div")
        conjuntoNombreVisa.setAttribute("class","conjunto-NombreVisa")
        divPadre.appendChild(conjuntoNombreVisa)

        const nombre = document.createElement("div")
        nombre.setAttribute("class","nombre")
        conjuntoNombreVisa.appendChild(nombre)

        const resultadoNombre = document.createElement("p")
        resultadoNombre.setAttribute("class","nombreUsuario")
        resultadoNombre.textContent = valoresNombre.value
        nombre.appendChild(resultadoNombre)

        const visa = document.createElement("div")
        visa.setAttribute("class","visa")
        conjuntoNombreVisa.appendChild(visa)
        const logoVisa = document.createElement("i")
        logoVisa.setAttribute("class","fa-brands fa-cc-visa")
        visa.appendChild(logoVisa)


        
        formularioTarjeta.reset();
})