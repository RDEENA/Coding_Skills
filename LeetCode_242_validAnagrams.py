#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# This has time complexity of nlogn as we are using inbuilt sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s:
            return False
        if sorted(s)==sorted(t):
            return True
# this code has time complexity of O(n) as we are using non nested for loop
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = {}
        for i in s:
            count[i]=count.get(i,0)+1
        for i in t:
            if i not in count or count[i]==0:
                return False
            count[i]-=1
        return all(count==0 for count in count.values())