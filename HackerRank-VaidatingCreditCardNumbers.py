a = int(input())
list1 = []
list2 = []
list3 = []
x = ""
b1=b2=b3=b4=""
for i in range(a):
    list1.append(input())

for j in list1:
    list3 = []
    if len(str(j)) < 16:
        list2.append("Invalid")
    
    elif len(str(j)) == 16:
        if j[0] == '4' or j[0] == '5' or j[0] == '6':
            #x = b1+b2+b3+b4
            for i in range(len(j)-4):
                if j[i] == j[i+1] == j[i+2] == j[i+3]:
                    list3.append("Invalid")
                else:
                    list3.append("Valid")
            if "Invalid" in list3:
                list2.append("Invalid")
            else:
                list2.append("Valid")
        else:
            list2.append("Invalid")
    else:
        if len(j) <= 19:
            b1,b2,b3,b4 = str(j).split("-")
            if (len(b1)+len(b2)+len(b3)+len(b4)) == 16 and len(b1) == len(b2) == len(b3) == len(b4):
                if j[0] == '4' or j[0] == '5' or j[0] == '6':
                    x = b1+b2+b3+b4
                    for i in range(len(x)-4):
                        if x[i] == x[i+1] == x[i+2] == x[i+3]:
                            list3.append("Invalid")
                        else:
                            list3.append("Valid")
                    if "Invalid" in list3:
                        list2.append("Invalid")
                    else:
                        list2.append("Valid")
                else:
                    list2.append("Invalid")
            else:
                list2.append("Invalid")
        else:
            list2.append("Invalid")
for i in range(a):
    print(list2[i])
