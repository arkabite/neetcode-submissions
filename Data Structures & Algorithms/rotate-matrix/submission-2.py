class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r=0,len(matrix)-1

        while l<r:
            for i in range(r-l):
                top,bottom=l,r

                # Storing the top left element
                topLeft=matrix[top][l+i]

                # Switching top left with bottom left
                matrix[top][l+i]=matrix[bottom-i][l]

                # Switching bottom left with bottom right
                matrix[bottom-i][l]=matrix[bottom][r-i]

                # Switching bottom left with top right
                matrix[bottom][r-i]=matrix[top+i][r]

                # Switching the top right with top left
                matrix[top+i][r]=topLeft

            l+=1
            r-=1

