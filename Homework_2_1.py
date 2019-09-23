s = str(input("Enter string \n"))
if s.isdigit():
    print("This string is digit")
print("Not digit string")
print("In this string is ", s.count(" "), " spaces")
print("In this string is ", s.count("."), " dots")
s2 = "Homework"
print(s2)
print("|", s2.center(100, " "), "|")
s3 = "beautiful is better than ugly."
print(s3)
print(s3.title())