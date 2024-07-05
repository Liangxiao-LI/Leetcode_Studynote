class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()
        sum = 0
        while sum != 1:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            
            n = sum
            
            if sum in temp:
                return False
            
            temp.add(n)

        return True