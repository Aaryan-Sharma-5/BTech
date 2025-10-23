// Problem 1.1 – Function Conversion
let num = Math.round(Math.random() * 10);
let name = "Aaryan";
const square = (num) => num * num;
console.log(square(num));
const greet = (name) => `Hello, ${name}`;
console.log(greet(name));

// Problem 1.2 – Using Arrow Functions with Array Methods
let numbers = [2, 4, 6, 8];
let doubled = numbers.map((num) => num * 2);
console.log(doubled);