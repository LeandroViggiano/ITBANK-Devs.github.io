const dropList = document.querySelectorAll("form select"),
  fromCurrency = document.querySelector(".from select"),
  toCurrency = document.querySelector(".to select"),
  getButton = document.querySelector("form button");

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
}

function loadFlag(element) {
  for (code in country_list) {
    if (code == element.value) {
      // si el código de moneda de la lista de países es igual al valor de la opción
      let imgTag = element.parentElement.querySelector("img"); // seleccionando la etiqueta img de una lista desplegable particular(osea los paises que en este caso puso dos)
      // pasa el código de país de un código de moneda seleccionado en una URL de img
      imgTag.src = `https://flagcdn.com/48x36/${country_list[
        code
      ].toLowerCase()}.png`;
    }
  }
}

window.addEventListener("load", () => {
  getExchangeRate();
});

getButton.addEventListener("click", (e) => {
  e.preventDefault(); //impido que el formulario se envíe
  getExchangeRate();
});

const exchangeIcon = document.querySelector("form .icon");
exchangeIcon.addEventListener("click", () => {
  let tempCode = fromCurrency.value; // código de moneda temporal de la lista desplegable FROM
  fromCurrency.value = toCurrency.value; // posar del De AL a.... y viceversa
  toCurrency.value = tempCode; // paso el código de moneda temporal al código de moneda de cambio
  loadFlag(fromCurrency); // llamando a loadFlag pasando el elemento de selección (fromCurrency) de FROM
  loadFlag(toCurrency); // llamando a loadFlag pasando el elemento de selección (toCurrency) de mone de cambio
  getExchangeRate(); // y lo mismo aca llamo a getExchangeRate
});
function getExchangeRate() {
  const amount = document.querySelector("form input");
  const exchangeRateTxt = document.querySelector("form .exchange-rate");
  let amountVal = amount.value;
  // si el usuario no ingresa ningún valor o ingresa 0, pondremos 1 valor por defecto en el campo de entrada. El avalor de partida por default es 1.
  if (amountVal == "" || amountVal == "0") {
    amount.value = "1";
    amountVal = 1;
  }
  exchangeRateTxt.innerText = "Obteniendo el cambio...";
  let concatStrings = splitString[0] + splitString[1],
    lastString = [5, 1, "a", 1],
    reverseString = lastString.reverse().join("");
  const apiKey = reverseString + concatStrings;
  let url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${fromCurrency.value}`;
  // fetching api respuesta y devolverlo con análisis en js obj y en otro método luego recibir ese obj
  //Basicamento lo que vismo en las clases declaro las promesas que tiene que devolverme un valor/resultado
  fetch(url)
    .then((response) => response.json())
    .then((result) => {
      let exchangeRate = result.conversion_rates[toCurrency.value]; // conseguir que el usuario seleccione el tipo de cambio
      let totalExRate = (amountVal * exchangeRate).toFixed(2); // multiplicar el valor ingresado por el usuario con el tipo de cambio seleccionado
      exchangeRateTxt.innerText = `${amountVal} ${fromCurrency.value} = ${totalExRate} ${toCurrency.value}`;
    })
    .catch(() => {
      // si el usuario está desconectado o se produjo cualquier otro error al obtener datos, se ejecutará la función de captura
      exchangeRateTxt.innerText = "Ups, algo salio mal";
    });
}
