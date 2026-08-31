class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Lowercase and keep only alphanumeric characters
        cleaned = [c for c in s.lower() if c.isalnum()]
        
        # 2. Check if it reads the same forward and backward
        return cleaned == cleaned[::-1]