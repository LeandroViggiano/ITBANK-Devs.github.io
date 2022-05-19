const $login = document.querySelector("main")
const getMain = (options) => {
    let {url, success, error} = options;

    (async () => {
        try {
            let res = await axios.get(url);

            let html = await res.data;

            success(html);
        } catch (err) {
            console.log(`Error: ${err.response.statusText}`)
        }
    })();
}

document.addEventListener("DOMContentLoaded", e => {
    getMain({
        url: "/ITBANK-Devs-Project/registro.html",
        success:(html) => $login.innerHTML = html,
        error: (err) => $login.innerHTML = err
    })
})


document.addEventListener("click", (e) => {
    if(e.target.matches("#continuar")){
        getMain({
            url: "/ITBANK-Devs-Project/registro-2.html",
            success:(html) => $login.innerHTML = html,
            error: (err) => $login.innerHTML = err
        })
    }
})

