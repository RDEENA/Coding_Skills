# Python program to find sum of numbers in the array which is equal to target value  given
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        #i is index and j is element (enumerate extracts both index and element from list)
        for i,j in enumerate(nums):
            difference = target - j
            if difference in result:
                return [result[difference],i]
            result[j]=i
# Here we are first taking an element and subtracting with the target value and finding whether the
# difference is present in the dictionary named result where it stores the value and its index .
#if present it will return the index else it will store the value of element and its index
#and proceed further.