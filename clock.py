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
