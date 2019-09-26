y = int(input("Enter year:"))

if (y % 4) or (not (y % 100) and (y % 400)):
    print("No")
else:
    print("yes")
#еле понял алгоритм, чего в календаре все так сложно ...