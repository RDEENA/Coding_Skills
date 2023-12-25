# check whether the given number is palindrome or not and return true if yes or false
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y[::-1] == y:
            return True
