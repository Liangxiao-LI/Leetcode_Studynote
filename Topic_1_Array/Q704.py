class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1 
        while right >= left:
            mid = int((right-left)/2) + left  
            if nums[mid] > target: # target in [left,mid)
                right = mid -1 
            elif nums[mid] < target: # target in (mid,right]
                left = mid + 1 
            else: 
                return mid
        return -1
