#1va zadacha
n = int(input("Въведете число n: "))

a, b = 1, 1
fib_list = []

while a <= n:
    fib_list.append(a)
    a, b = b, a + b

print(fib_list)
