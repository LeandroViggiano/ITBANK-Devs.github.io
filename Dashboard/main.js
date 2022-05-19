const hamburger = document.getElementById("menu");
const panel = document.querySelector(".izquierda");

hamburger.addEventListener("click", (e) => {
    panel.classList.toggle("block")
    hamburger.classList.toggle("block")
})