#2ra zadacha
n = int(input("Въведете число n: "))

divisors = []
for i in range(1, n + 1):
    if n % i == 0 and i % 2 != 0:
        divisors.append(i)

print(divisors)
