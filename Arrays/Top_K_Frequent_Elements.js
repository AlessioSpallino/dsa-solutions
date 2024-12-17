/**
 * This function finds the top K frequent elements in an array using a variant of Bucket Sort.
 * 
 * Bucket Sort Variant Explanation:
 * 1. **Step 1**: Count the frequency of each unique number using a hashmap.
 * 2. **Step 2**: Use a "bucket array" where the index represents the frequency
 *    and the value at each index is a list of numbers with that frequency.
 * 3. **Step 3**: Traverse the bucket array from the highest frequency down to collect
 *    the most frequent elements until K elements are collected.
 * 
 * @param {number[]} nums - Array of integers.
 * @param {number} k - Number of top frequent elements to return.
 * @return {number[]} - Array containing the top K frequent elements.
 */
function topKFrequent(nums, k) {
    const valueMap = {}; // Step 1: Map to count the frequency of each number.
    const fArr = [];     // Step 2: Bucket array to store numbers by frequency.
    const result = [];   // Array to store the final top K frequent elements.

    // Step 1: Count the frequency of each number using a hashmap.
    for (const num of nums) {
        valueMap[num] = (valueMap[num] || 0) + 1;
    }

    // Step 2: Populate the bucket array.
    // The index in fArr represents the frequency, and its value is a list of numbers with that frequency.
    for (const [n, c] of Object.entries(valueMap)) {
        if (!fArr[c]) fArr[c] = []; // Initialize the bucket if it doesn't exist.
        fArr[c].push(n);            // Add the number to the appropriate frequency bucket.
    }

    // Step 3: Collect the top K frequent elements by traversing the bucket array from the back.
    // Start from the highest possible frequency (nums.length) and move downwards.
    for (let i = nums.length; i >= 0; i -= 1) {
        const values = fArr[i]; // Get the list of numbers at this frequency.
        if (values) {
            values.forEach((el) => result.push(el)); // Add numbers to the result array.
        }
        if (result.length === k) return result; // Stop when we have K elements.
    }

    return result; // Return the result (should never reach this line because K is guaranteed).
}
