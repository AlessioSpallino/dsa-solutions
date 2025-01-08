from typing import List

class Solution:
    def subset(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  # Get the length of the input array
        res = []  # To store all subsets
        sol = []  # Temporary list to build each subset
        
        def backtrack(i):
            # Base case: If we've processed all elements
            if i == n:
                value = sol[:]  # Create a copy of the current subset
                res.append(value)  # Add the current subset to the result
                return
            
            # Recursive case 1: Exclude the current element and move to the next
            backtrack(i + 1)
            
            # Recursive case 2: Include the current element
            sol.append(nums[i])  # Add the current element to the subset
            backtrack(i + 1)  # Move to the next element with the current one included
            sol.pop()  # Undo the inclusion to backtrack and explore other possibilities
        
        backtrack(0)  # Start the backtracking process from the first element
        return res  # Return all subsets
    
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    nums = [1, 2, 3]  # Input array for which subsets are to be generated
    result = solution.subset(nums)  # Call the subset function
    print(result)  # Print the resulting list of subsets
