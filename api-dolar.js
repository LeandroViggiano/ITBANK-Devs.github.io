const container = document.querySelector(".container"),
dolares = document.querySelector(".dolares"),
oficial = document.querySelector(".oficial"),
blue = document.querySelector(".blue"),
contado = document.querySelector(".contado")

function api() {
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(data => data.json())
    .then(data => {
        oficial.innerHTML = ` <b>${data[0].casa.nombre}</b><br> Compra: ${data[0].casa.compra} | Venta: ${data[0].casa.compra}`

        blue.innerHTML = ` <b>${data[1].casa.nombre}</b><br> Compra: ${data[1].casa.compra} | Venta: ${data[1].casa.compra}`

        contado.innerHTML = ` <b>${data[3].casa.nombre}</b><br> Compra: ${data[3].casa.compra} | Venta: ${data[3].casa.compra}`
    })  


}
api()

setInterval(() => {
    api()
}, 5000);


/* CONVERTIR */

const form = document.querySelector(".formulario"),
inputPesos = document.querySelector(".pesos"),
listaDolares = document.getElementById("listaDolares"),
resultadoCambio = document.querySelector(".resultadoCambio")

form.addEventListener("submit", (e) => {
    e.preventDefault()
    
    if (form.listaDolares.value === "Dolar Oficial"){
        const compra = document.querySelector(".oficial").innerHTML

        let indice = compra.indexOf(":")
        let indice2 = compra.lastIndexOf("Venta")

        let extraer = compra.substring(indice+ 2, indice2-1)
        let listo = extraer.replace(",", ".")
        
        resultadoCambio.innerHTML = Number(listo) * inputPesos.value
        console.log(resultadoCambio)

    }

    if (form.listaDolares.value === "Dolar Blue"){
        const compra = document.querySelector(".blue").innerHTML

        let indice = compra.indexOf(":")
        let indice2 = compra.lastIndexOf("Venta")

        let extraer = compra.substring(indice+ 2, indice2-1)
        let listo = extraer.replace(",", ".")
        
        resultadoCambio.innerHTML = Number(listo) * inputPesos.value

    }

    form.reset()
})