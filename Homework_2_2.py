import math

print("Triangle\na = 179 \nb = 971\nc = ", (179 ** 2 + 971 ** 2) ** 0.5)
print("Triangle with \"math\" \na = 179 \nb = 971\nc = ", math.sqrt(179 ** 2 + 971 ** 2))

d1 = 35
print("In digit ", d1, " is ", d1 // 10, " ten")

d2 = 735
print("long way to calculate sum of digits\r")
a = d3 = d2 % 10
b = d3 = d3 % 10
c = d3 = d3 % 10
print(a + b + c)

print("short way to calculate sum of digits")
print(math.fsum(list(map(int, str(d2)))))

n = int(input("Enter number \n"))
n1 = n + 1
while n1 % 2:
    n1 = n1 + 1
print("You enter ", n, " next even number is ", n1)

n = float(input("Enter float number \n"))
print(n)
print("Fractional part: ", str(n).rsplit(".", 2)[1])

if (len(str(n).rsplit(".", 2)[1])) > 1:
    print("Digit on second after \".\" ", (str(n).rsplit(".", 2)[1])[1])
else:
    print("No digit on second after \".\" in this number")
