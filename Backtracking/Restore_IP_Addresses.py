class Solution(object):
    def restoreIpAddresses(self, s):
        """
        Restore all valid IP addresses from a given string.
        
        :type s: str
        :rtype: List[str]
        """
        res = []  # List to store the valid IP addresses

        def backtracking(i=0, string=[], count=0):
            """
            Backtracking function to explore all possible IP address segments.

            :param i: Current index in the string `s`.
            :param string: List of segments in the current IP address.
            :param count: Number of segments added to the current IP address.
            """
            # Base case: If we have 4 segments and used the entire string, it's a valid IP
            if count == 4 and i == len(s):
                res.append(".".join(string))  # Join the segments with dots and add to result
                return

            # If we've added 4 segments but haven't consumed the whole string, or vice versa
            if count >= 4 or i >= len(s):
                return 
            
            # Try to extract segments of size 1 to 3
            for step in range(1, 4):
                # Ensure we don't go out of bounds
                if i + step <= len(s):
                    segment = s[i:i+step]  # Extract a substring of length `step`
                    
                    # Validate the segment:
                    # - No leading zeros unless the segment is "0".
                    # - The segment value must be <= 255.
                    if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
                        continue  # Skip invalid segments
                    
                    # Recur with the next index, updated string, and incremented count
                    backtracking(i + step, string + [segment], count + 1)            

        # Start the backtracking process from the first character
        backtracking()
        return res
