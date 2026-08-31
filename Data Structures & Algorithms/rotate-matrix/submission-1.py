class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r=0,len(matrix)-1

        while l<r:
            for i in range(r-l):
                top,bottom=l,r

                #storing the topleft variable
                topLeft=matrix[top][l+i]

                # Switching topleft with bottom left
                matrix[top][l+i]=matrix[bottom-i][l]

                if not (l<r and top<bottom):
                    break
                
                #switching bottom left with bottom right
                matrix[bottom-i][l]=matrix[bottom][r-i]

                #switching the bottom right with the top right
                matrix[bottom][r-i]=matrix[top+i][r]

                #switchin the top right with the toplef
                matrix[top+i][r]=topLeft
            l+=1
            r-=1