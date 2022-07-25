class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        result = -1
        number = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    if number < (nums[j] + nums[i]) < k:
                        number = nums[j] + nums[i]
                    
        if number == 0:
            return result
        
        else:
            return number
