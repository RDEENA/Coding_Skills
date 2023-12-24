class Solution:
    def minOperations(self, s: str) -> int:
        count1,count0=0,0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=="0":
                   count1+=1
                else:
                    count0+=1
            elif i%2==1:
                if s[i]=="1":
                    count1+=1
                else:
                    count0+=1
        return min(count0,count1)