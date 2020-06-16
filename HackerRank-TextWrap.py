s = input()
w = int(input())
s1 = len(s)
a= ""
while s1 >= 0:
    if len(s) < w:
        for j in range(len(s)):
            a = a+s[j]
    else:
        for i in range(w):
            a = a+s[i]
    
    print(a)
    a = ""
    s1 = s1-w
    s = s[w:]
