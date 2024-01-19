#rat count house
n = 0
def rat_count(r,unit,n,arr):
    if (n == '\0'):
        print("number of houses is 0")
        return -1
    required = r*unit
    food_sum = 0
    count = 0
    for i in range(n):
        if food_sum >= required:
            return count
        else:
            food_sum += arr[i]
            count+=1
    if(food_sum<required):
        return 0

    return count
r = int(input("number of rats"))
units =  int(input("number of units"))
arr = []
n = int(input("enter the number of houses"))

for i in range(n):
    arr.append(int(input("enter the food amount")))
res =  rat_count(r,units,n,arr)
if(res == 0):
    print("food not sufficient")
print("Number of house to be traverse",res)
