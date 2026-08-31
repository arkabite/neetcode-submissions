class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r=0,len(matrix)-1

        while l<r:
            for i in range(r-l):
                top,bottom=l,r

                topLeft=matrix[top][l+i]

                # Replacing topLeft with the bottom left element
                matrix[top][l+i]=matrix[bottom-i][l]

                # Replacing the bottom left with the bottom right element
                matrix[bottom-i][l]=matrix[bottom][r-i]

                # Replacing the bottom right with the top right element
                matrix[bottom][r-i]=matrix[top+i][r]

                # Replacing the top right with the topLeft element
                matrix[top+i][r]=topLeft
            l+=1
            r-=1



