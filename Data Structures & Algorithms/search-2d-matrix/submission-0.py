class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        for i in matrix:
            if target>i[-1]:
                continue
            else:
                n=len(i)
                l=0
                r=n-1
                while l<=r:
                    m=l+(r-l)//2
                    if i[m]==target:
                        return True
                    
                    if i[m]>target:
                        r=m-1
                    elif i[m]<target:
                        l=m+1
        
        return False
