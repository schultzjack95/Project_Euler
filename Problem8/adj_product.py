filename = "input.txt"
step = 13

# Parameter n is a string of 13 digits
# Returns the product of those 13 digits
def product(n):
    prod = 1
    for i in n:
        prod *= int(i)
    return prod

def __main__():
    with open(filename) as f:
        content = f.readlines()
    
    max_product = 0
    sstring = ""
    
    cont = ""
    # Trim content to one continuous string
    for line in content:
        cont += line[0:-1]
    content = cont
    
    print(content)
    
    for i in range(len(content)-step):
        prod = product(content[i:i+step])

        if prod > max_product:
            max_product = prod
            sstring = content[i:i+step]

    print(f"Product: {max_product}")
    print(f"Input digits: {sstring}")

if __name__ == "__main__":
    __main__()
