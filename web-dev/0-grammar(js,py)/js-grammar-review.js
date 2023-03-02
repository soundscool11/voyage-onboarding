// Data Type (null vs undefined)
let name1 = null
console.log(name1) // null

let name2
console.log(name2) // undefined



// String Concat
console.log('My' + ' car') // My car
console.log('1' + 2) // 12

// Template Literals
const shoesPrice = 200
console.log(`The price of this shoes is ${shoesPrice}.`)

// Numeric Operators
console.log(10 ** 2) // exponential

// Equality Operators
console.log(1 === '1') // strict (value + data type): false
console.log(1 == '1') // true



// Function Declaration
function calculateAvg(price1, price2) {
    const sum = price1 + price2
    console.log(`The sum of two products is ${sum}`)
    const avg = sum / 2
    return avg
}

// Function Call
const p1 = 1000
const p2 = 2000
const avg = calculateAvg(p1, p2)
console.log(`The average price of two products is ${avg}`)



// Class - reusable
class Notebook {
    constructor(name, price, company) {
        this.name = name
        this.price = price
        this.company = company
    }

    // Method
    printInfo() {
        console.log(`Product name: ${this.name}, Price: ${this.price} won`)
    }
}

// Object
const notebook1 = new Notebook('Mac', 2000000, 'Apple')

console.log(notebook1)
console.log(notebook1.name)
console.log(notebook1.price)
console.log(notebook1.company)

notebook1.printInfo()

// Object Literal: creating object without declaring Class template - quick and simple
const computer = {
    name: 'Samsung Book2 Pro',
    price: 2000000,
    printInfo: function () {
        console.log(`Product name: ${this.name}, Price: ${this.price} won`)
    }
}

computer.printInfo()

// Practice
class Clothes {
    constructor(color, size, price) {
        this.color = color
        this.size = size
        this.price = price
    }

    printInfo() {
        console.log(`Color: ${this.color}, size: ${this.size}, price: ${this.price}`) 
    }
}

const skirt = new Clothes('black', 'S', 20000)
const pants = new Clothes('Gray', 'M', 30000)

skirt.printInfo()
pants.printInfo()



// Array
const arr1 = new Array(1, 2, 3, 4, 5) // creating object (by using Array build-in class)
const arr2 = [1, 2, 3, 4, 5]
console.log(arr2.length)
arr1.push(6) // adding the value at the end of the array
arr1.pop() // removing the last value

for(let i = 0; i < arr2.length; i++) {
    console.log(arr2[i]) // new line
}

for(const num of arr1) {
    console.log(num)
}