#13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum1 = 0

        for i in range(len(s)):
            if i < len(s) - 1 and val[s[i]] < val[s[i + 1]]:
                sum1 -= val[s[i]]
            else:
                sum1 += val[s[i]]
        return sum1
