class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left >= 0:
            mid = left + (right-left)%2
            if target < nums[mid]: # in [left,mid - 1)
                right = mid - 1
            elif target > nums[mid]: #in (left,right]
                left = mid + 1
            else:
                return mid
        return left