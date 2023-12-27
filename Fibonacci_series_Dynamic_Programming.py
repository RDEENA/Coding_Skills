# Finding fibonacci series of a given number using dynamic programming approach
# traditional method

import time
'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-2) + fib(n-1)
start = time.time()
res = fib(35)
final = time.time()
print(res,final-start)'''

# dynamic programming approach
import time
def fib(n):
    F=[0]*n

    if (n<=1):
       return n
    else:
        F[0] = 0
        F[1] = 1
        for i in range(2,n):
            F[i] = F[i-2]+F[i-1]
        return F[n-1]
start = time.time()
res  = fib(100)
final = time.time()
print(res,final-start)