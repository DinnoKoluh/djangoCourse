// Javascript objects are just classes
var carInfo = {
    make:"Toyota", 
    year:"1444", 
    model:"somw",
    fun: function(a) {
        return a*this.year;
    }    
}

console.log(carInfo["make"])
console.log(carInfo.make)

for (key in carInfo) {
    console.log(carInfo[key])
}

console.log(carInfo.fun(4))

// sa npm install <package> instaliramo biblioteke 
// npm init pravi json file u kojem se cuvaju info o bibliotekama