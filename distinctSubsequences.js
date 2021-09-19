/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function (s, t) {
  let sLength = s.length;
  let tLength = t.length;
  const arr = Array(tLength).fill(0);

  for (let i = sLength - 1; i >= 0; i--) {
    let prev = 1;
    for (let j = tLength - 1; j >= 0; j--) {
      let cur = arr[j];
      if (s[i] === t[j]) {
        arr[j] += prev;
      }
      prev = cur;
    }
  }
  return arr[0];
};

console.log(numDistinct('rabbbit', 'rabbit'));
console.log(numDistinct('babgbag', 'bag'));