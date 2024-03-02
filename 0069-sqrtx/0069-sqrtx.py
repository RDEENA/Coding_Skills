class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i, j = 1, x
        res = 0
        while i <= j:
            mid = (i + j) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                i = mid + 1
                res = mid
            else:
                j = mid - 1
        return res
