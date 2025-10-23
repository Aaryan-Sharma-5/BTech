// Problem 2.1 – Execute a Callback
function greetUser(name, callback) {
  console.log(`Welcome, ${name}!`);
  callback();
}

greetUser("Aaryan", function() {
  console.log("Callback executed!");
});

// Problem 2.2 – Custom Array Processor
function processArray(arr, callback) {
  let result = [];
  for(let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i]));
  }
  return result;
}

processArray([1, 2, 3], function(num) {
  console.log(num * 10);
});

