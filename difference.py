def findCount(arr,length,num,diff):
    count = 0
    for i in range(length):
        if(arr[i]-num <= diff):
            count +=1
        else:
            continue
    return count


length = int(input("size of array"))
arr = []
print("enter the array elements")
for i in range(length):
    val = int(input())
    arr.append(val)
num = int(input("enter the number"))
diff = int(input("enter the difference"))
res = findCount(arr,length,num,diff)
print(res)

