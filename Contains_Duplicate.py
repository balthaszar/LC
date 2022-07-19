'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        setty = set(nums)
        l = len(setty)
        ll = len(nums)
        
        if l == ll:
            return False
        
        else:
            return True
        