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
print("fsum", math.fsum(list(map(int, str(d2))))) # map принимает в себя фукнцию и список и применяет
# указанную функцию к всем элементам списка, там ище есть муть с лямбдами но это пока не победил.
# В данном действии для метода fsum нужен массив цифр, вот и преобразили сначала число в строку (а строка это массив)
# а каждый символ строки отдельно в число через мап, так же можно было серез for но через мап кошернее

print("sum", sum(list(map(int, str(d2))))) # да можно ище через встроенную функцию получить сумму,
# но она так же принимает в себя итерируемый список, не из библиотеки math, но тоже вариант

n = int(input("Enter number \n"))
if n % 2:
    print("You enter ", n, " next even number is ", n + 1)
else:
    print("You enter ", n, " next even number is ", n + 2)
# переделано на использование условия

n = float(input("Enter float number \n"))
print(n)
print("Fractional part: ", str(n).rsplit(".", 2)[1])
print("Fractional part v.2: ", n - n // 1) #метод "через математику", получение остатка
#но из за битовых сдвигов получаем не совсем то

#убрал проверку вообще, не правильно понял условие, брал второй знак после точки, а по условию нужно первый
print("Digit on second after \".\" ", (str(n).split(".", 2)[1])[0])
print("Digit on second after \".\" via v.2 ", str(n % 1)[2])
# метод "через математику", получение остатка от деления, преобразуем в строку, берем второй символ
# 4 элемент так как 1 - это 0, второй - делитель, третий нас не интересует


# rsplit в списке методов при алфавитной сортировке иднт раньше ) поэтому заюзан он


