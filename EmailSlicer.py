n = int(input("Enter the number of email addresses you want to enter: "))
dict1 = dict()
list1 = []
for i in range(n):
    list1.append(input("Email Adress: "))
for i in list1:
    username,dom = i.split("@")
    domain,waste = dom.split(".")
    dict1[username] = domain
print(dict1)
