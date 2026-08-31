class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to bound our numbers
        mask = 0xFFFFFFFF
        # The maximum positive value for a 32-bit signed integer
        max_int = 0x7FFFFFFF
        while b!=0:
            temp=((a&b)<<1)&mask
            a=(a^b)&mask
            b=temp

        return a if a<=max_int else ~(a^mask)