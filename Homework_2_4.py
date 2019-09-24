abc = []
while len(abc) < 3:
    abc.append(int(input("Enter triangle side:")))
abc.sort()
if (abc[0] + abc[1]) > abc[2]:
    print("Triangle with sides a = ", abc[0], ", b = ", abc[1], ", c = ", abc[2], " is possible")
else:
    print("Triangle with sides a = ", abc[0], ", b = ", abc[1], ", c = ", abc[2], " is NOT possible")
print(abc)
