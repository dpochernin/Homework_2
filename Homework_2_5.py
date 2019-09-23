list_1 = []
while len(list_1) < 3:
    list_1.append(int(input("Enter number:")))
a = list_1[0]
b = list_1[1]
c = list_1[2]
list_1.sort()
print("Sorted numbers via list method", list_1)

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("Sort via \"if\" method", a, b, c)