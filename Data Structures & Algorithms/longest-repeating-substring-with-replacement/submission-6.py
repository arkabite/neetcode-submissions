class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Tracks character frequencies in the current window
        l = 0
        res = 0
        max_freq = 0  # Tracks the highest frequency of any single character in the window
        
        for r in range(len(s)):
            # Add the current character to our window count
            count[s[r]] = count.get(s[r], 0) + 1
            
            # Update the max frequency seen in the current window
            max_freq = max(max_freq, count[s[r]])
            
            # Current window length is (r - l + 1)
            # If cells to replace > k, the window is invalid. Shrink it from the left.
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            # The window is guaranteed valid here, track the max size
            res = max(res, r - l + 1)
            
        return res