function swapText() {
    let text1 = document.getElementById("paragraph1").textContent;
    let text2 = document.getElementById("paragraph2").textContent;
    let text3 = document.getElementById("paragraph3").textContent;

    document.getElementById("paragraph1").textContent = text2;
    document.getElementById("paragraph2").textContent = text3;
    document.getElementById("paragraph3").textContent = text1;
}

function plus() {
    let counter = document.getElementById("counter");
    counter.textContent = currentCount + 1;
}

function reset() {
    let counter = document.getElementById("counter");
    counter.textContent = "0";
}

function minus() {
    let counter = document.getElementById("counter");
    counter.textContent = currentCount - 1;
}

function changeToGreen() {
    document.getElementById("paragraph1").style.color = "green";
    document.getElementById("paragraph2").style.color = "green";
    document.getElementById("paragraph3").style.color = "green";
}

function changeToRed() {
    document.getElementById("paragraph1").style.color = "red";
    document.getElementById("paragraph2").style.color = "red";
    document.getElementById("paragraph3").style.color = "red";
}

function changeToYellow() {
    document.getElementById("paragraph1").style.color = "yellow";
    document.getElementById("paragraph2").style.color = "yellow";
    document.getElementById("paragraph3").style.color = "yellow";
}

function carInfo(brand, model, year, color, engine) {
    let sentence =brand + model + year + color + engine;
    return sentence;
}

const myFavFilms = {
    name: "The Maze Runner",
    genre: "action",
    releaseYear: 2015
}

