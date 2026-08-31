class Solution:
    def longestPalindrome(self, s: str) -> str:
        minLen=0
        res=""

        for i in range(len(s)):
            # for odd length palindromes
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if ((r-l)+1)>minLen:
                    minLen=((r-l)+1)
                    res=s[l:r+1]
                l-=1
                r+=1
            # for even length palindromes
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if ((r-l)+1)>minLen:
                    minLen=((r-l)+1)
                    res=s[l:r+1]
                l-=1
                r+=1
        
        return res