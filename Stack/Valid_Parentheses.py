class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        matching_brackets = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        opening_brackets = set(matching_brackets.values())  # {'(', '[', '{'}

        for char in s:
            if char in opening_brackets:  # Check if it's an opening bracket
                result.append(char)
            else:
                if not result:  # Check if result is empty
                    return False
                if matching_brackets[char] != result.pop():  # Check the last opening bracket
                    return False

        return len(result) == 0  # Check if all brackets are matched
