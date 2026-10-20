class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""

        for i in strs:
            wordLen=len(i)
            prefix=str(wordLen)+"#"+i
            res+=prefix
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the '#' character
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length (handles multi-digit lengths like "15#")
            length = int(s[i:j])
            
            # The word starts right after '#' and goes for `length` characters
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move `i` to the start of the next encoded string
            i = end
            
        return res
