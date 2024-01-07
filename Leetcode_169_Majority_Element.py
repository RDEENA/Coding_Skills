#Given an array nums of size n, return the majority element.
#he majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        count = 0
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in dict1:
                dict1[num] += 1
                if dict1[num] > len(nums) / 2:
                    return num

            else:
                dict1[num] = 1

        return -1


# or
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
