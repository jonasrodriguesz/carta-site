const textos = document.querySelectorAll("p");

textos.forEach((texto, index) => {

    texto.style.opacity = "0";

    setTimeout(() => {

        texto.style.transition = "opacity 2s";

        texto.style.opacity = "1";

    }, index * 1500);

});