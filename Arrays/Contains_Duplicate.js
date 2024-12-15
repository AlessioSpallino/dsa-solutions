/**
* @param {number[]} nums
* @return {boolean}
*/

function hasDuplicate(nums) {
    const map = {};

    for (let i = 0; i < nums.length; i += 1) {
        const number = nums[i];
        if (!map[number]) { map[number] = true; continue; }

        return true
    }

    return false
}
