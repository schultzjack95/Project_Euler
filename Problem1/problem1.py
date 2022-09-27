def isDivisible(num, divisors):
    for d in divisors:
        if num% d == 0:
            return True
    return False

total = 0

for i in range(1000):
    if isDivisible(i, [3, 5]):
        total += i

print(total)
