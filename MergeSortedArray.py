class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """


        mn = len(nums1) - n
        z = len(nums2) - 1
        q = 0

        while (mn < len(nums1)) and  (q <=z):
            nums1[mn] =nums2[q]
    
            mn += 1
            q += 1
    
        nums1.sort()
        
        return nums1