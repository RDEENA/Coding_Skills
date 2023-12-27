# Longest Common Prefix
# we need to find the longest string repeating in all the given string
def find_string(s):
    min_len = min(len(s[0]), len(s[len(s) - 1]))
    rep = ""
    for i in range(min_len+1):
        j = 0
        if j<(len(s)-1):
           if(s[0][:i])==(s[j+1][:i]):
              rep = s[0][:i]
              j+=1
    if not rep:
        return -1
    return rep

s = ["INDIAISMARVELOUS","INDIAISINCREDIBLE","INDIAISBEAUTIFUL"]
res = find_string(s)
print(res)

# using sorting
def find_string(s):
    if not s:
        return ""
    s.sort()
    first_str, last_str = s[0], s[-1]
    min_len = min(len(first_str), len(last_str))
    i = 0
    while i < min_len and first_str[i] == last_str[i]:
        i += 1

    return first_str[:i] if i > 0 else -1
s = ["geeksforgeeks", "geeoss", "geekjis"]
result = find_string(s)
print(result)

# or you can use inbuilt function
import os
s = ["geeksforgeeks", "geeoss", "geekjis"]
m = os.path.commonprefix(s)
print(m)