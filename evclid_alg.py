a = float(input("Enter first number pls: "))
b = float(input("Enter second number pls: "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)