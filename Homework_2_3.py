y = int(input("Enter year:"))

if not (y % 100):
    print("No")
elif not (y % 4) or not (y % 400):
    print("yes")
else:
    print("No")
