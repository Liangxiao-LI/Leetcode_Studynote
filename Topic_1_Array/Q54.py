class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startx = 0
        starty = 0

        row = len(matrix) #rows
        col = len(matrix[0]) #column
        mini = min(row,col)
        loop = mini//2

        result = [0] * (row*col)
        index = 0

        for offset in range(1, loop+1):
            for i in range(starty,col - offset): #从左到右，左闭右开
                result[index] = matrix[startx][i]
                index += 1
            for i in range(startx,row - offset): #从上到下，上闭下开
                result[index] = matrix[i][col - offset]
                index += 1
            for i in range(col - offset , starty, -1): #从右到左，右闭左开
                result[index] = matrix[row-offset][i]
                index += 1
            for i in range(row - offset, startx, -1): #从下到上，下闭上开
                result[index] = matrix[i][starty]
                index += 1

            startx += 1
            starty += 1

        if mini %2 ==1:
            if row >= col:
                for i in range(startx,row - loop):
                    result[index] = matrix[i][starty]
                    index += 1
            else: 
                for i in range(starty,col - loop):
                    result[index] = matrix[startx][i]
                    index += 1
        return result
