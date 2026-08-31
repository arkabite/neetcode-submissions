class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1=len(s)
        n2=len(t)
        counter1=Counter(s)
        counter2=Counter(t)
        if counter1==counter2:
            return True
        else:
            return False