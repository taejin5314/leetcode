var checkIfExist = function (arr) {
  let map = new Set();

  for (let i = 0; i < arr.length; i++) {
    if (map.has(arr[i] * 2) || map.has(arr[i] / 2)) {
      return true;
    }
    map.add(arr[i]);
  }

  return false;
};

console.log(checkIfExist([10, 2, 5, 3]));
console.log(checkIfExist([7, 1, 14, 11]));
console.log(checkIfExist([3, 1, 7, 11]));