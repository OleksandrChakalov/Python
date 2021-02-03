fib0 = fib1 = 1
element = input('Ведіть порядковий номер числа, яке ви шукаєте: ')
element = int(element)
for n in range(int(element - 2)):
    fib0, fib1 = fib1, fib1+fib0
print(str(element) + ' елемент дорівнює ' + str(fib1))
