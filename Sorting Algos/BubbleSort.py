Bubble Sort:-
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares 
adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

Some Notes:-
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

# Bubble Sort Algorithm
import random
n = int(input("Enter the length of the list: "))
list1 = [random.randint(10,100) for i in range(n)]
print(list1)
for i in range(1,n):
    for j in range(i):
        if list1[i]<list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
