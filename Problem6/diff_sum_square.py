def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i*i
    return total

def square_of_sums(n):
    total = n * (n+1) / 2
    return total * total

def __main__():
    n = 100
    diff = square_of_sums(n) - sum_of_squares(n)
    print(diff)

if __name__ == "__main__":
    __main__()
