class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize arrays to hold prefix and postfix products
        pre = [0] * len(nums)  # Prefix products
        post = [0] * len(nums)  # Postfix products
        res = [0] * len(nums)  # Result array

        # Calculate prefix products
        for i, num in enumerate(nums):
            if i == 0:
                pre[i] = nums[i]  # First element is its own prefix product
            else:
                pre[i] = nums[i] * pre[i - 1]  # Current prefix is the current number times the previous prefix

        # Calculate postfix products in reverse order
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if i == len(nums) - 1:
                post[i] = num  # Last element is its own postfix product
            else:
                post[i] = num * post[i + 1]  # Current postfix is the current number times the next postfix

        # Build the result array using the prefix and postfix products
        for i, num in enumerate(nums):
            if i == 0:
                res[i] = post[i + 1]  # For the first element, use the first postfix product
            elif i == len(nums) - 1:
                res[i] = pre[i - 1]  # For the last element, use the last prefix product
            else:
                # For other elements, multiply the corresponding prefix and postfix products
                res[i] = pre[i - 1] * post[i + 1]

        return res
