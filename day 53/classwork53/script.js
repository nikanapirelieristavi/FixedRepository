//1
const firstParagraph = document.getElementById('p1').textContent;
const lastParagraph = document.getElementById('p5').textContent;

console.log("First paragraph: " + firstParagraph);
console.log("Last paragraph: " + lastParagraph);

//2
const me = {
    age: 15,
    name: "nika",
    surname: "napireli-eristavi"
}
const myFriend = {
    age: 15,
    name: "luka",
    surname: "Tsivilashvili"
}

//3
function addition(num1, num2){
    console.log(num1 + num2)
}
function subtraction(num1, num2){
    console.log(num1 - num2)
}
function multiplication(num1, num2){
    console.log(num1 * num2)
}
function division(num1, num2){
    console.log(num1 / num2)
}

//4
function greet(name){
    return("hello " + name )
}

//5
function mathOperation(num1,num2,num3){
    const result = (num1 + num2) / num3
}

//6
function evenOrOdd(num){
    const rezult = num % 2 == 0
}

//7


const car = {
    name: "something",
    model: "idk",
    year: 2020,
    start: function(){
        console.log("starting")
    },
    break: function(){
        console.log("breaking")
    }
}