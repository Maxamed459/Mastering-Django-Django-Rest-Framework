document.addEventListener("DOMContentLoaded", () => {
  alert("your js is running successfully");
});

const hello = () => {
  alert("Hello, welcome to django Static and Assets");
};


// two sum
const twoSum = (arr, target) => {
  for (let i = 0; i < arr.length; i++){
    for (j = i; j < arr.length; j++) {
      if ([i] + [j] === target) {
        console.log(i, j);
        return i, j
      }
      // console.log("please enter valid numbers")
    }
  }
}

console.log(twoSum([1, 2, 3, 4, 5], 6));