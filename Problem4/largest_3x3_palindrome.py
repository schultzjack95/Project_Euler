def isPalindrome(num):
    str_num = str(num)
    return str_num[:] == str_num[::-1]


def __main__():
    max_num = 0;
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if isPalindrome(num):
                if num > max_num:
                    max_num = num
    print(max_num)



if __name__ == "__main__":
    __main__()
