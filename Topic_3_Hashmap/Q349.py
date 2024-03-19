class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        int_dict = defaultdict(int)

        for n in nums1:
            int_dict[n] = 1
        
        for n in nums2:
            if int_dict[n] == 1:
                int_dict[n] = 2

        result = []

        for key in list(int_dict.keys()):
            if int_dict[key] == 2:
                result.append(key)
        return result