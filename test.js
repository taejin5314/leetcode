var time = function (n) {
  var t0 = performance.now();
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
  fib(n);
  console.log(performance.now() - t0);
}

time(35)