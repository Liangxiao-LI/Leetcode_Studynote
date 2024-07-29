class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict

        ran_dict = defaultdict(int)
        mag_dict = defaultdict(int)

        for k in ransomNote:
            ran_dict[k] += 1
        
        for k in magazine:
            mag_dict[k] += 1
        
        for k in ran_dict:
            if mag_dict[k] - ran_dict[k] < 0:
                return False
        
        return True
    
nums = [1,2,3,4]

len(nums)

for i in range(len(nums)):
    print(i)

5 //2