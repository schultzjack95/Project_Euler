class FibonacciComputer:
    prev = 0
    current = 1

    iteration = 0

    def advance(self):
        self.prev, self.current = self.current, self.prev + self.current
        self.iteration += 1
    


fc = FibonacciComputer()
total = 0

while (fc.current <= 4000000):
    fc.advance()
    if fc.current % 2 == 0:
        total += fc.current

print(total)
