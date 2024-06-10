from functools import lru_cache


class Fibonacci:
    def __init__(self):
        self.x = 0

    @lru_cache
    def fib(self, n):
        if n <= 2:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        return self.fib(self.x)
    
