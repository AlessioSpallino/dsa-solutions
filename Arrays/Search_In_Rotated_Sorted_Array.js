/**
* @param {number[]} nums
* @param {number} target
* @return {number}
*/

function search(nums, target) {
    const length = nums.length;
    let left = 0;
    let right = length - 1;

    while (left <= right) {
        const mid = Math.floor((right + left) / 2);

        if (nums[mid] == target) { return mid; }

        if (nums[left] <= nums[mid]) {
            // left side is sorted
            if (nums[left] <= target && nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // right side is sorted
            if (nums[mid] < target && nums[right] >= target) {
                left = mid + 1
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}
