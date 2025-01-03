import heapq

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        max_freq = 0
        char_count = dict()
        
        # Build a dictionary to store the frequency of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            max_freq = max(max_freq, char_count[char])

        # Check if the input string can be reorganized
        # If the most frequent character appears more than half the length of the string (rounded up),
        # it's impossible to reorganize the string without adjacent duplicates.
        if max_freq > (len(s) - max_freq) + 1:
            print("No solution")
            return result

        # Create a max heap to store characters based on their frequencies
        # Python's `heapq` is a min-heap by default, so we use negative frequencies for a max-heap
        heap = []
        for key in char_count.keys():
            heapq.heappush(heap, (-char_count[key], key))

        # Keep track of the previously used character to avoid consecutive usage
        prev = None
        while heap:
            freq, char = heapq.heappop(heap)
            result += char  # Append the current character to the result
            # Re-add the previous character to the heap if it still has remaining frequency
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            # Update `prev` to the current character with reduced frequency
            if freq + 1 < 0:
                prev = (freq + 1, char)

        return result
