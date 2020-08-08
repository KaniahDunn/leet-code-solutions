


//Happy Number
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
// 
//  @param {number} n
//  @return {boolean}
//  
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