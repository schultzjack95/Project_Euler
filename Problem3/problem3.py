#num = 600851475143


#magnitude = 6.0e11
#so the square root is < 1e6?
#1e6 = 1000000
#1e6 ^2 = 1000000 000000
# so we perform a sieve of eratosthenes to find primes up to 1e6,
#   which is guaranteed to find at least one of each pair of factors.

# List of size 1e6

class SieveOfEratosthenes:

    # Create a sieve of given size, without checking prime-ness.
    # First item in sieve (index 0) represents 1, 
    #   the second item (index 1) represents 2, and so on.
    # Thus integer n can be find at sieve[n-1].
    # 1 is trivially prime and is ignored for the algorithm.
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.index = 1 
        self.sieve = [True] * size
        self.primes = []

    # Process sieve to find the next prime, and set all multiples of that number to False.
    # Do this by advancing index by 1 until something marked as Prime is found,
    #   adding it to the list of primes, then marking all multiples as NotPrime.
    def _findNextPrime(self):
        try:
            finished = self._prepareNextPrimeIndex()
            if finished:
                return
            self.primes.append(self.index)
            #print(f"Found prime number {self.index}!")
            k = 2
            while(k * self.index < self.size):
                self.sieve[k * self.index] = False
                k += 1
        except IndexError:
            print(f"Error accessing index {self.index} in list size {self.size}")

    # Advance index to the next valid index.
    # Returns True if index is at the end of the list, False if otherwise
    def _prepareNextPrimeIndex(self):
        self.index += 1
        while (self.index < self.size):
            if self.sieve[self.index] == True:
                #print("Found index", self.index)
                return False
            #print(f"Index {self.index} is not prime. Checking next index...")
            self.index += 1
        return True

    def runSieve(self):
        while self.index < self.size:
            self._findNextPrime()


sieve = SieveOfEratosthenes(1000000)

sieve.runSieve()

num = 600851475143
prime_divisors = []

for div in sieve.primes:
    if div > num:
        break
    while num % div == 0:
        prime_divisors.append(div)
        greatest_prime_factor = div
        num /= div
        
print(prime_divisors)
print(greatest_prime_factor)
