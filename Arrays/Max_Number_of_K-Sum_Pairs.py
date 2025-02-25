class Solution(object):
    def maxOperations(self, nums, k):
        sumMap = {}
        op = 0

        for num in nums:
            diff = k - num
            if num in sumMap and sumMap[num] > 0:
                op+=1
                sumMap[num] -=1
            else:
                sumMap[diff] = sumMap.get(diff, 0) + 1


        return op