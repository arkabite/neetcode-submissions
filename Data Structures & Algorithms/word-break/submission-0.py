class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set()
        maxWord=0
        for i in wordDict:
            words.add(i)
            maxWord=max(maxWord,len(i))
        
        memo={}
        
        def dfs(start):
            # Base Case: If we've successfully reached the end of the string
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]

            # Try prefixing every possible word length from the 'start' pointer
            # We don't need to check prefixes longer than max_word_len
            for end in range(start + 1, min(len(s) + 1, start + maxWord + 1)):
                prefix = s[start:end]
                
                # If the prefix is a valid word, check if the REST of the string is valid
                if prefix in words:
                    if dfs(end):  # Move the start pointer to the end of this word
                        memo[start] = True
                        return True

            # If no prefix split works out, this start position is a dead end
            memo[start] = False
            return False

        return dfs(0)