/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    const map = {};

    for (let i = 0; i < nums.length; i += 1) {
        const currentValue = nums[i];
        const valueToSearch = target - currentValue;

        if (map.hasOwnProperty(valueToSearch)) {
            return [map[valueToSearch], i];
        }

        map[currentValue] = i;
    }

    return [];
}
