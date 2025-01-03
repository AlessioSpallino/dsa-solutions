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
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            max_freq = max(max_freq, char_count[char])

        if(max_freq > (len(s) - max_freq) + 1):
            print("This cannot work")
            return result

        heap = []
        for key in char_count.keys():
            heapq.heappush(heap, (-1 * char_count[key], key))

        prev = None
        while(heap):
            freq, char = heapq.heappop(heap)
            result += char
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if(freq + 1 < 0):
                prev = (freq + 1, char)

        return result