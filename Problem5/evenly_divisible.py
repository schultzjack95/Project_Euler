from math import sqrt
from pprint import pprint

def isFullyDivisible(num):
    for i in range(2, 20):
        if num % i != 0:
            return False
    return True

def findFactors(num):
    lst = []
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            lst.append( (i, int(num/i)) )
    return lst


def __main__():
    #true answer is 232792560, found by:
    # 4 * 4 * 5 * 7 * 9 * 11 * 13 * 17 * 19
    factors_list = []
    for i in range(2,21):
        factors_list.append(findFactors(i))
    pprint([(i+2,x) for i,x in enumerate(factors_list)])
    num = 232_792560
    flag = True
    while (flag):
        print(f"Trying {num}.")
        if isFullyDivisible(num):
            print(num)
            flag = False
        num += 1
        


if __name__ == "__main__":
    __main__()
