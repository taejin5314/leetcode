var fib = function (n) {
  if (n === 0 || n === 1) {
    return n;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
};

console.log(fib(2));
console.log(fib(3));
console.log(fib(4));
console.log(fib(5));
console.log(fib(6));
console.log(fib(7));

// 1 1 3 5 9 15 25 41 67 109 177