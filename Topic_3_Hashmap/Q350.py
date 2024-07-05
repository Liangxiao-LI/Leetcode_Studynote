class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        int_dict1 = defaultdict(int)
        int_dict2 = defaultdict(int)
        for n in nums1:
            int_dict1[n] += 1
        
        for n in nums2:
            int_dict2[n] += 1

        set1 = set(int_dict1)
        set2 = set(int_dict2)
        common_elements = list(set1.intersection(set2))

        result = []

        for common in common_elements:
            if int_dict1[common] > int_dict2[common]:
                for i in range(int_dict2[common]):
                    result.append(common)
            else:
                for i in range(int_dict1[common]):
                    result.append(common)
        return result


# Create two defaultdicts with integer defaults
dd1 = defaultdict(int)
dd2 = defaultdict(int)

# Assume both defaultdicts have been populated with some integer counts
dd1['a'],dd1['b'],dd1['c'] = 5,3,10
dd2['a'] = 2
dd2['b'] = 4
dd2['d'] = 1

print(dd1)
print(set(dd1))

