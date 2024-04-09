class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 != 0:
                return False
            else:
                n //= 2
        if n == 1:
            return True

    # I go through the number and check if it is divisible by 2, if so, I divide it by 2 and continue,
    # otherwise, I return False.
    # Finally, I check if the number is 1, if so, I return True, otherwise, I return False.
