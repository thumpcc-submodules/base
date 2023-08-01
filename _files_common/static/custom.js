document.addEventListener("DOMContentLoaded", function (event) {
    const elems = document.querySelectorAll('a.external');
    elems.forEach(elem => {
        elem.setAttribute("target", "_blank");
    })
});