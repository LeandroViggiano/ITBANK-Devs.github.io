const d = document,
errorMensaje = d.querySelector(".error-mensaje"),
errorContraseña = d.querySelector(".error-password")
form = d.querySelector(".formulario"),
submit = d.getElementById("submit"),
usuario = d.querySelector(".usuario"),
password = d.querySelector(".password"),
ver = d.getElementById("ver"),
cerrar = d.getElementById("cerrar");

const regUsuario = /^[a-zA-Z]+$/i,
regPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}/;

form.addEventListener("submit", (e) => {

    if(!regUsuario.test(usuario.value)){
        e.preventDefault();
        errorMensaje.style.setProperty("visibility","visible")
    } else {
        errorMensaje.style.setProperty("visibility","hidden")
    }

    if(usuario.value.length === 0){
        e.preventDefault();
        errorMensaje.style.setProperty("visibility","visible")
    }

    if(!regPassword.test(password.value)){
        e.preventDefault();
        errorContraseña.style.setProperty("visibility","visible")
    } else {
        errorContraseña.style.setProperty("visibility","hidden")
    }

    if(password.value.length === 0){
        e.preventDefault();
        errorContraseña.style.setProperty("visibility","visible")
    }

})

document.addEventListener("keyup",(e) => {
    if(e.target.matches(".usuario")){

        if(!regUsuario.test(usuario.value)){
            e.preventDefault();
            errorMensaje.style.setProperty("visibility","visible")
        } else {
            errorMensaje.style.setProperty("visibility","hidden")
        }

        if (usuario.value.length === 0) {
            errorMensaje.style.setProperty("visibility","hidden")
            e.preventDefault();
        };
    }
})


document.addEventListener("click", (e) => {

    if(e.target.matches("#ver")){
        password.type = "text";

        ver.style.setProperty("display","none")
        cerrar.style.setProperty("display","block")
    }
    
    if(e.target.matches("#cerrar")){
        password.type = "password";
        cerrar.style.setProperty("display","none")
        ver.style.setProperty("display","block")
    }
})


