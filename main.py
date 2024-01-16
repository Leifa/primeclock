class Clock:
    def __init__(self, n):
        self.n = n
        self.rows = [0]

    def step(self):
        self.rows[0] += 1
        i=0
        while self.rows[i] == self.n:
            self.rows[i] = 0
            i += 1
            if i == len(self.rows):
                self.rows.append(0)
            self.rows[i] += 1

    def set(self, k):
        self.rows = [k%self.n]
        k //= self.n
        while k != 0:
            self.rows.append(k%self.n)
            k //= self.n

    def get_multiplicity(self):
        for i in range(len(self.rows)):
            if self.rows[i] != 0:
                return i
        return None

c2 = Clock(2)
clocks = [c2]
for i in range(1, 931):
    prime_factorization = []
    # Tick all the clocks
    for c in clocks:
        c.step()
        prime_factorization.extend([c.n]*c.get_multiplicity())

    # Add the remaining factor
    rest = i
    for d in prime_factorization:
        rest //= d
    if rest > 1:
        prime_factorization.append(rest)

    # If the number is prime, start a new clock
    if len(prime_factorization) == 1 and i > 2:
        c = Clock(i)
        c.set(i)
        clocks.append(c)

    print(f"{i} = {prime_factorization}")

