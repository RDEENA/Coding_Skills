#75. Sort Colors
#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,k,j=0,0,len(nums)-1
        while(i<=j):
            if nums[i]==0:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            else:
                i+=1