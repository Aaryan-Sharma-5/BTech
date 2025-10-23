const math = require('./math-module');
console.log('Custom Module Demonstration: Math Operations\n');
console.log(`Addition: 15 + 7 = ${math.add(15, 7)}`);
console.log(`Subtraction: 20 - 8 = ${math.subtract(20, 8)}`);
console.log(`Multiplication: 6 * 4 = ${math.multiply(6, 4)}`);
console.log(`Division: 100 ÷ 5 = ${math.divide(100, 5)}`);
console.log(`Power: 3⁴ = ${math.power(3, 4)}`);
console.log(`Modulo: 17 % 3 = ${math.modulo(17, 3)}`);

console.log('\nError Handling:');
try {
    math.divide(10, 0);
} catch (error) {
    console.log(`Division by zero: ${error.message}`);
}

console.log('\nCustom module demonstration completed!');