const container = document.querySelector(".container"),
dolares = document.querySelector(".dolares"),
oficial = document.querySelector(".oficial"),
blue = document.querySelector(".blue"),
contado = document.querySelector(".contado")

function api() {
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(data => data.json())
    .then(data => {
        oficial.innerHTML = ` <b>${data[0].casa.nombre}</b><br> Compra: ${data[0].casa.compra} | Venta: ${data[0].casa.venta}`

        blue.innerHTML = ` <b>${data[1].casa.nombre}</b><br> Compra: ${data[1].casa.compra} | Venta: ${data[1].casa.venta}`
    })  


}
api()

setInterval(() => {
    api()
}, 5000);

/* CONVERTIDOR */

const dropList = document.querySelectorAll(".cambio form select"),
fromCurrency = document.querySelector(".cambio .from select"),
toCurrency = document.querySelector(".cambio .to select"),
getButton = document.querySelector(".enviar");
const eeu = document.querySelector(".eeu")
const arg = document.querySelector(".arg")

getButton.addEventListener("click", (e) => {
    if ((eeu.getAttribute("src") == 'https://flagcdn.com/48x36/us.png')){
    getExchangeRate1()
  }

  if ((eeu.getAttribute("src") == 'https://flagcdn.com/48x36/ar.png')){
    getExchangeRate2()
  }
});

/*
for (let i = 0; i < dropList.length; i++) {
  for (currency_code in country_list) {
    // seleccionando USD por defecto como moneda FROM y ARG
    let selected =
      i == 0
        ? currency_code == "USD"
          ? "selected"
          : ""
        : currency_code == "ARS"
        ? "selected"
        : "";
    // creando una etiqueta de opción pasando el código de moneda como texto y valor
    let optionTag = `<option value="${currency_code}" ${selected}>${currency_code}</option>`;
    // inserto la etiqueta de opciones dentro de la etiqueta de selección
    dropList[i].insertAdjacentHTML("beforeend", optionTag);
  }
  dropList[i].addEventListener("change", (e) => {
    loadFlag(e.target); // llamando a loadFlag pasando el elemento de destino como argumento
  });
}*/

function loadFlag(element) {
  for (code in country_list) {
    if (code == element.value) {
      // si el código de moneda de la lista de países es igual al valor de la opción
      let imgTag = element.parentElement.querySelector(".cambio img"); // seleccionando la etiqueta img de una lista desplegable particular(osea los paises que en este caso puso dos)
      // pasa el código de país de un código de moneda seleccionado en una URL de img
      imgTag.src = `https://flagcdn.com/48x36/${country_list[
        code
      ].toLowerCase()}.png`;
    }
  }
}

window.addEventListener("load", () => {
  //getExchangeRate();
});



const exchangeIcon = document.querySelector("form .icon")

exchangeIcon.addEventListener("click", () => {

  if (eeu.getAttribute("src") == 'https://flagcdn.com/48x36/us.png'){
    eeu.setAttribute("src", "https://flagcdn.com/48x36/ar.png")
  } else if (eeu.getAttribute("src") == 'https://flagcdn.com/48x36/ar.png'){
    eeu.setAttribute("src", "https://flagcdn.com/48x36/us.png")
  }

  if (arg.getAttribute("src") == 'https://flagcdn.com/48x36/ar.png'){
    arg.setAttribute("src", "https://flagcdn.com/48x36/us.png")
  } else {
    arg.setAttribute("src", "https://flagcdn.com/48x36/ar.png")
  }

  if ((eeu.getAttribute("src") == 'https://flagcdn.com/48x36/us.png') && (arg.getAttribute("src") == 'https://flagcdn.com/48x36/ar.png')){
    getExchangeRate1()
  }

  if ((eeu.getAttribute("src") == 'https://flagcdn.com/48x36/ar.png') && (arg.getAttribute("src") == 'https://flagcdn.com/48x36/us.png')){
    getExchangeRate2()
  }
});
function getExchangeRate1() {
  const amount = document.querySelector(".cambio form input");
  const exchangeRateTxt = document.querySelector(".cambio form .exchange-rate");
  let amountVal = amount.value;
  // si el usuario no ingresa ningún valor o ingresa 0, pondremos 1 valor por defecto en el campo de entrada. El avalor de partida por default es 1.
  if (amountVal == "" || amountVal == "0") {
    amount.value = "1";
    amountVal = 1;
  }
  exchangeRateTxt.innerText = "Obteniendo el cambio...";
  /*let concatStrings = splitString[0] + splitString[1],
    lastString = [5, 1, "a", 1],
    reverseString = lastString.reverse().join("");
  const apiKey = reverseString + concatStrings;*/
  //let url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${fromCurrency.value}`;
  // fetching api respuesta y devolverlo con análisis en js obj y en otro método luego recibir ese obj
  //Basicamento lo que vismo en las clases declaro las promesas que tiene que devolverme un valor/resultado
  fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then((data) => data.json())
    .then((data) => {
        let dolarOficial = data[0].casa.venta
        console.log(data.casa)
        let punto = dolarOficial.replace(',', '.')
        exchangeRateTxt.innerHTML = amountVal * Number(punto)
    })
    .catch(() => {
      // si el usuario está desconectado o se produjo cualquier otro error al obtener datos, se ejecutará la función de captura
      exchangeRateTxt.innerText = "Ups, algo salio mal";
    });
}

function getExchangeRate2() {
    const amount = document.querySelector(".cambio form input");
    const exchangeRateTxt = document.querySelector(".cambio form .exchange-rate");
    let amountVal = amount.value;
    // si el usuario no ingresa ningún valor o ingresa 0, pondremos 1 valor por defecto en el campo de entrada. El avalor de partida por default es 1.
    if (amountVal == "" || amountVal == "0") {
      amount.value = "1";
      amountVal = 1;
    }
    exchangeRateTxt.innerText = "Obteniendo el cambio...";
    /*let concatStrings = splitString[0] + splitString[1],
      lastString = [5, 1, "a", 1],
      reverseString = lastString.reverse().join("");
    const apiKey = reverseString + concatStrings;*/
    //let url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${fromCurrency.value}`;
    // fetching api respuesta y devolverlo con análisis en js obj y en otro método luego recibir ese obj
    //Basicamento lo que vismo en las clases declaro las promesas que tiene que devolverme un valor/resultado
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
      .then((data) => data.json())
      .then((data) => {
          let dolarOficial = data[0].casa.venta
          let punto = dolarOficial.replace(',', '.')
          exchangeRateTxt.innerHTML = amountVal / Number(punto) 
      })
      .catch(() => {
        // si el usuario está desconectado o se produjo cualquier otro error al obtener datos, se ejecutará la función de captura
        exchangeRateTxt.innerText = "Ups, algo salio mal";
      });
  }


/* ABRIR CONVERSOR DE MONEDA */
const convertor = document.querySelector(".convertor")
const conversor = document.querySelector(".conversor")
convertor.addEventListener("click", ()=> {
    conversor.classList.add('abrirConversor')
    conversor.classList.remove('cerrarConversor')

})

/* CERRAR CONVERSOR DE MONEDA */
const cerrar = document.querySelector(".cerrar")
cerrar.addEventListener("click", (e) => {
    conversor.classList.add('cerrarConversor')
    conversor.classList.remove('abrirConversor')

})