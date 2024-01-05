# rotate the array k times with O(1) time complexity
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%(len(nums))
        if k>0:
            nums.reverse()
            nums[:k]=nums[:k][::-1]
            nums[k:]=nums[k:][::-1]
