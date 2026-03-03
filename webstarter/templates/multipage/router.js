// webstarter/templates/multipage/router.js
console.log("Módulo de navegación WebStarter cargado");

export function navigateTo(page) {
    window.location.href = `${page}.html`;
}