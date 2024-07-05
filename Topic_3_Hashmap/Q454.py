from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        
        sum1 = defaultdict(int)
        sum2 = defaultdict(int)

        for i in nums1:
            for j in nums2:
                sum1[i+j] += 1
        for i in nums3:
            for j in nums4:
                sum2[i+j] += 1

        ans = 0

        for key1 in sum1:
            for key2 in sum2:
                if key1+key2 == 0:
                    ans+= sum1[key1]*sum2[key2]
        
        return ans