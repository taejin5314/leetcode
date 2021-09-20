// var time = function (n) {
//   var t0 = performance.now();
//   var fib = function (n) {
//     let cur, prev = 1, prevPrev = 0;
//     if (n === 0 || n === 1) {
//       return n;
//     } else {
//       for (let i = 2; i <= n; i++) {
//         cur = prev + prevPrev;
//         prevPrev = prev;
//         prev = cur;
//       }
//       return cur;
//     }
//   };
//   fib(n);
//   console.log(performance.now() - t0);
// }

var time = function (n) {
  var t0 = performance.now();
  const map = { 0: 1, 1: 1 }
  var fib = function (n, map) {
    if (!map[n]) {
      return map[n] = fib(n - 2, map) + fib(n - 1, map);
    } else {
      return map[n]
    }
  };
  console.log(fib(n, map));
  console.log(performance.now() - t0);
}

// const map = { 1: 1, 2: 1 }
// var fib = function (n, map) {
//   if (!map[n]) {
//     map[n] = fib(n - 2, map) + fib(n - 1, map);
//     return map[n]
//   } else {
//     return map[n]
//   }
// };

var fib = function (n) {
  let arr = new Array(n);
  arr[0] = 1;
  arr[1] = 1;

  if (n === 0 || n === 1) {
    return arr[n];
  } else {
    for (let i = 2; i <= n; i++) {
      arr[i] = arr[i - 2] + arr[i - 1];
    }
    return arr[n];
  }
}

console.log(fib(35))

// time(35)