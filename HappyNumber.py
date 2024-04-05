class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = sum([int(i) ** 2 for i in str(n)])

        return n == 1

    # While n is not 1 and n is not 4, meaning the number it's not a happy number
    # Calculate the sum of the square of the digits of n, by taking the sum for each n in str(n) and squaring it
