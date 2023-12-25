from typing import List


# program to remove  duplicates from a sorted array and order should be preserved
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur_pos = 1
        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[cur_pos] = nums[i]
                cur_pos += 1
        return cur_pos
