import random
n = int(input("Enter the length of the list: "))
list1 = [random.randint(10,100) for i in range(n)]
print(list1)
for i in range(1,n):
    for j in range(i):
        if list1[i]<list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
