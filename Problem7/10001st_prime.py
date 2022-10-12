from math import sqrt

def isPrime(n):
    for i in range(2, int( sqrt(n)+1 )):
        if n % i == 0:
            return False
    return True

def __main__():
    # Skipping 2, and all subsequent even numbers.
    count = 1
    num = 3
    
    while count != 10001:
        if isPrime(num):
            count += 1
        num += 2

    pass
    print(num - 2)

if __name__ == "__main__":
    __main__()
