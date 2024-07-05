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

        for i in nums1:
            for j in nums2:
                sum1[i+j] += 1

        ans = 0

        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in sum1:
                    ans += sum1[-n3-n4]
        
        return ans