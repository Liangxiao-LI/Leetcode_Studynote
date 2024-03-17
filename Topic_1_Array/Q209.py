class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = 0
        window_sum = 0
        min_length = float('inf')
        while right_pointer < len(nums):
            window_sum += nums[right_pointer]
            right_pointer += 1
            while window_sum >= target:
                min_length = min(min_length,right_pointer - left_pointer)
                window_sum -= nums[left_pointer]
                left_pointer += 1

        if min_length == float('inf'):
            return 0

        return min_length