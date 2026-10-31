class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            temp=nums1
            nums1=nums2
            nums2=temp
        
        n1=len(nums1)
        n2=len(nums2)
        totalHalf=(n1+n2)//2
        l=0
        r=n1-1
        while True:
            i=l+(r-l)//2
            j=totalHalf-i-2

            L1=nums1[i] if i>=0 else float("-inf")
            R1=nums1[i+1] if (i+1)<n1 else float("inf")
            L2=nums2[j] if j>=0 else float("-inf")
            R2=nums2[j+1] if (j+1)<n2 else float("inf")

            if L1<=R2 and L2<=R1:
                if (n1+n2)%2==0:
                    return (max(L1,L2)+min(R1,R2))/2
                else:
                    return min(R1,R2)
            
            if L1>R2:
                r=i-1
            else:
                l=i+1
