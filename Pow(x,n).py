class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

    # If n == 0, return 1
    # If n == 1, return x
    # If n == -1, return 1 / x, turning the problem into a positive one
    # If n is even, return x^(n/2) * x^(n/2)
    # If n is odd, return x * x^(n/2) * x^(n/2)
