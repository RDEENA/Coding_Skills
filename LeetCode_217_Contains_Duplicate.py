#Given an integer array nums, return true if any value appears at least twice in the array,#
# and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1= {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]]=1
            else:
                return True
        return False