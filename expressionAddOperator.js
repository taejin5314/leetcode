/**
 * @param {string} num
 * @param {number} target
 * @return {string[]}
 */
var addOperators = function (num, target) {
  const result = [];
  backtracking(num, target, 0, 0, "", 0, 0, result);
  return result;
};

var backtracking = function (num, target, index, sum, expression, curNum, prevNum, result) {
  if (index > num.length) {
    return;
  }

  if (index === num.length && sum === target && curNum === 0) {
    result.push(expression.slice(1));
    return;
  }

  const newNum = 10 * curNum + (+num[index]);
  if (newNum > 0) {
    backtracking(num, target, index + 1, sum, expression, newNum, prevNum, result);
  }

  backtracking(num, target, index + 1, sum + newNum, expression + '+' + newNum, 0, +newNum, result);

  if (expression.length > 0) {
    backtracking(num, target, index + 1, sum - newNum, expression + '-' + newNum, 0, -newNum, result);
    const multSum = sum - prevNum + (prevNum * newNum);
    backtracking(num, target, index + 1, multSum, expression + '*' + newNum, 0, (prevNum * newNum), result);
  }
  return;
}

console.log(addOperators('123', 6));
console.log(addOperators('232', 8));
console.log(addOperators('105', 5));
console.log(addOperators('00', 0));
console.log(addOperators('3456237490', 9191));