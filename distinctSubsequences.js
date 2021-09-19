/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function (s, t) {
  for (let i = 0; i < s.length - t.length; i++) {
    let count = 0;
    for (let j = 0; j < t.length; j++) {
      if (s[i] === t[j]) {
        count++;
      }
    }
  }
};