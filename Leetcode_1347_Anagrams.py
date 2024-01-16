#1347. Minimum Number of Steps to Make Two Strings Anagram
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if not s:
            return 0

        count1 = {}
        count2 = {}
        for i in s:
            count1[i] = count1.get(i, 0) + 1
        for j in t:
            count2[j] = count2.get(j, 0) + 1
        count = 0
        for a, b in count1.items():
            count += max(0, b - count2.get(a, 0))
        return count

