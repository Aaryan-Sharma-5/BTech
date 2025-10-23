// Problem 3.1 – Simple Promise Handling
function loadData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data Loaded");
    }, 2000);
  });
}

loadData().then((result) => {
  console.log(result);
});

// Problem 3.2 – Simulate an API Call
function fakeFetch(url){
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(`Data fetched from ${url}`);
    }, 3000);
  });
}

fakeFetch("https://api.example.com").then(console.log);
