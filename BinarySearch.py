import random
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

n = int(input("Enter the length of the list: "))
list1 = [random.randint(10,100) for i in range(n)]
list1.sort()
print(list1)
a = int(input("Enter the element to be searched: "))
result = binary_search(list1,0,len(list1)-1,a)

if result != -1:
    print("The element is present at index",result)
else:
    print("The element is not present in the list.")
