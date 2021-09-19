// var fib = function (n) {
//   if (n === 0 || n === 1) {
//     return n;
//   } else {
//     return fib(n - 1) + fib(n - 2);
//   }
// };

var fib = function (n) {
  let cur, prev = 1, prevPrev = 0;
  if (n === 0 || n === 1) {
    return n;
  } else {
    for (let i = 2; i <= n; i++) {
      cur = prev + prevPrev;
      prevPrev = prev;
      prev = cur;
    }
    return cur;
  }
};

console.log(fib(0));
console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(4));
console.log(fib(5));
console.log(fib(6));
console.log(fib(7));
console.log(fib(500));

// 1 1 3 5 9 15 25 41 67 109 177