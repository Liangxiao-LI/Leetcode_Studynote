class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx = 0
        starty = 0
        loop = n // 2
        value = 1

        for offset in range(1,loop+1):
            for i in range(starty, n-offset): #从左至右，左闭右开
                nums[startx][i] = value
                value += 1
            for i in range(startx, n - offset): #从上至下, 上闭下开
                nums[i][n-offset] = value
                value += 1
            for i in range(n-offset, starty, -1): #从右至左，右闭左开
                nums[n-offset][i] = value
                value += 1
            for i in range(n-offset, startx, -1): #从下至上，下闭上开
                nums[i][starty] = value
                value += 1
            startx += 1
            starty += 1

        if n % 2 != 0:
            nums[n//2][n//2] = value
        
        return nums