class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        # Use Float Division to make sure we return a calculation error less than 10-5
        max_avg = float(current_sum) / k
        left = 0

        for right in range(k, len(nums)):
            current_sum-=nums[left]
            current_sum+=nums[right]
            left+=1
            
            # Use Float Division to make sure we return a calculation error less than 10-5
            max_avg = max(max_avg, float(current_sum) / k)

        return max_avg