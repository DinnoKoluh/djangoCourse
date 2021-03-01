// alert("Welcom motherfuckerrr!")
// aaa = prompt("Enter something")
// alert("You entered " + aaa)

// 2 === "2" to get the logic all the way (value and data type)
// null and undefined as data types

document.querySelector("#head1") // grabbing elements by CSS syntax .class and h1 

var myHead = document.getElementById("head1");
var par = document.getElementById("p1");

function randomColor () {
    var hexCode = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
        color = color + hexCode[Math.floor(Math.random()*16)]
        }
    return color;
}

function changeHeadColor () {
    color = randomColor();
    myHead.style.color = color;
    //par.textContent = "Hex Code is: " + color;
}


//setInterval("changeHeadColor()", 1000)

// How to affect text on the Web page
// par.innerHTML
par.addEventListener('mouseover', changeHeadColor);
par.addEventListener("mouseout", function() {
    myHead.style.color = 'black';
})
par.addEventListener('click', changeHeadColor);


par.textContent = "Some new text. And the Current Hex Code is " + randomColor(); 

console.log(par.textContent);

//myHead.onclick("changeHeadColor()")
// myHead.style.color = 'red';
// myHead.style.color = 'blue';
