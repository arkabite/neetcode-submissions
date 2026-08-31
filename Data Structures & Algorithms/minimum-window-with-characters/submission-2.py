from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
            
        count1 = Counter(t)
        count = defaultdict(int)
        
        sett = set(t)
        required_matches = len(sett) # Total unique chars to match
        mon = 0                      # Unique chars currently matching required freq
        
        # Track the best window found so far
        min_len = float("inf")
        best_window = (0, 0)
        
        l = 0
        # Expand the window using the right pointer 'r'
        for r in range(len(s)):
            char_r = s[r]
            count[char_r] += 1
            
            # If we reached the exact required frequency for this character
            if char_r in sett and count[char_r] == count1[char_r]:
                mon += 1
                
            # Shrink the window from the left as long as it remains valid
            while mon == required_matches:
                # Update our minimum window snapshot
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    best_window = (l, r + 1) # r + 1 for clean string slicing later
                
                # Pop the left character out of the window
                char_l = s[l]
                count[char_l] -= 1
                
                # If removing this character breaks our required frequency match
                if char_l in sett and count[char_l] < count1[char_l]:
                    mon -= 1
                    
                l += 1 # Move the left boundary forward
                
        # If min_len never changed, no valid window was found
        return "" if min_len == float("inf") else s[best_window[0] : best_window[1]]