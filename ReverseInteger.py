class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int(str(x)[1:][::-1]) * -1
        else:
            x = int(str(x)[::-1])

        if x > 2**31-1 or x < -2**31:
            return 0
        else:
            return x

    # Firstly, I check if the integer is negative, if so, I remove the negative sign and reverse the integer,
    # and then add the negative sign back to the reversed integer.
    # Otherwise, I reverse the integer.

    # Thereafter, I check if the reversed integer is within the range of a 32-bit signed integer,
    # if not, I return 0.
    # Otherwise, I return the reversed integer.
