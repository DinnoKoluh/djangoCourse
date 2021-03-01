const prompt = require('prompt-sync')();


console.log("Dinno");
/*alert("Yo WhaaasUp") */

// 2 ** 4 = 16, 16 % 5 = 1

str1 = "dinno";
console.log(str1);
var a = str1.length;
console.log(a);

var nothing = null;

// var variable = prompt("Enter a number: ");
// console.log(variable);

if (10 > 14) {
    console.log("fefef");
}
else{
    console.log("gegeg");    
}

// while(true) {
//     console.log("ffef")
// }

for (var i = 0; i<str1.length; i++){
    console.log("Current Number Is: " + str1[i]);
}

function fun1(a=5) {
    return a*a;
}

console.log(fun1(4));

var nums = new Array(1, 2, 4);

console.log(nums[1])

str1[3] = "z";
console.log(str1)

nums.pop()

console.log(nums)

function printMe (a) {
    console.log(a);
}
words = ["sana", "una", "unac"]
words.forEach(printMe);

for (var i = 0; i < nums.length; i++) {
    console.log(nums[i])
}
