
// TWO SUM
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:

// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].


//   @param {number[]} nums
//   @param {number} target
//   @return {number[]}

const twoSum = function (nums, target) {
    const comp = {};
    for (let i = 0; i < nums.length; i++) {
        if (comp[nums[i]] >= 0) {
            return [comp[nums[i]], i]
        }
        comp[target - nums[i]] = i
    }
};

/**Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let newArr = nums.sort(function (a, b) { return a - b });
    let num = 0;
    for (let i = 0; i < newArr.length; i++) {
        if (newArr.indexOf(newArr[i]) === newArr.lastIndexOf(newArr[i])) {
            num = newArr[i];
        }
    }
    return num;
};

/*Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

*/
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n, seen) {
    let sum = 0;
    if (seen === undefined) {
        seen = []
    }
    const digitString = n.toString();
    for (let i = 0; i < digitString.length; i++) {
        let sqr = Math.pow(parseInt(digitString[i]), 2);
        sum += sqr
    }
    if (sum === 1) {
        return true;
    } else if (seen.includes(sum)) {
        return false;
    }
    seen.push(sum);
    return isHappy(sum, seen);
};