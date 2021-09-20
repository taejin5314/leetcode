var validMountainArray = function (arr) {
  let left = 0;
  let right = arr.length - 1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[left] < arr[left + 1]) {
      left++;
    }
    if (arr[right - 1] > arr[right]) {
      right--;
    }

    if (left === right && left !== 0 && right !== 0 && left !== arr.length - 1 && right !== arr.length - 1) {
      return true;
    }
  }
  return false;
};

console.log(validMountainArray([2, 1]));
console.log(validMountainArray([3, 5, 5]));
console.log(validMountainArray([0, 3, 2, 1]));