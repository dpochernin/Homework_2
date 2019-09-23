list_1 = []
while len(list_1) < 3:
    list_1.append(int(input("Enter number:")))
i = 0
if list_1[0] == list_1[1] or list_1[1] == list_1[2] or list_1[0] == list_1[2]:
    i = 2
if list_1[0] == list_1[1] == list_1[2]:
    i = 3
print("In list is ", i, "mach digits")
