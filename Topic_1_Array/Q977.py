class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        Forward_pointer = 0
        Backward_pointer = len(nums) - 1
        result = [0] * len(nums)
        input_pointer = len(nums) - 1
        while input_pointer >= 0:
            if nums[Forward_pointer]**2 < nums[Backward_pointer]**2 :
                result[input_pointer] = nums[Backward_pointer]**2
                Backward_pointer -= 1
            else:
                result[input_pointer] = nums[Forward_pointer]**2
                Forward_pointer += 1
            input_pointer -= 1
        
        return result
