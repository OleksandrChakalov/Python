fib0 = fib1 = 1
n = int(input("Please enter number: "))
if n <= 0:
    print("Please try one more time")

else:
    print(fib0, fib1, end=" ")
    for i in range(n):
        fib0, fib1 = fib1, fib1+fib0
        print(fib1, end=" ")