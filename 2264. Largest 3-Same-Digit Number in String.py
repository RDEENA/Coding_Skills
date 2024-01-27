'''2264. Largest 3-Same-Digit Number in String
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.


Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.'''
import re
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l1 = ['111', '222', '333', '444', '555', '666', '777', '888', '999', '000']
        res = []
        int_arr = []

        for i in range(len(num) - 2):
            if num[i:i + 3] in l1:
                res.append(num[i:i + 3])

        if not res:
            return ""

        if all(int(x) == 0 for x in res):
            return '000'

        for i in res:
            int_arr.append(int(i))

        res = max(int_arr)
        return str(res)
# or
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max(re.findall(r'(\d)\1\1', num) or [""]) * 3