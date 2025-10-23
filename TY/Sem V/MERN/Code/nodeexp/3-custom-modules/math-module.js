const arithmetic = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
  divide: (a, b) => {
    if (b === 0) {
      throw new Error('Division by zero is not allowed');
    }
    return a / b;
  },
  power: (base, exponent) => Math.pow(base, exponent),
  modulo: (a, b) => a % b
};

module.exports = {
  arithmetic,
  add: arithmetic.add,
  subtract: arithmetic.subtract,
  multiply: arithmetic.multiply,
  divide: arithmetic.divide,
  power: arithmetic.power,
  modulo: arithmetic.modulo
};
