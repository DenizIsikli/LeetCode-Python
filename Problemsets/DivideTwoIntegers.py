class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == -1 and dividend == -2**31:
            return 2**31-1
        else:
            if dividend < 0 or divisor < 0:
                return int(dividend/divisor)
            else:
                return int(dividend/divisor)

    # Firstly I check if the divisor is -1 and the dividend is -2^31, meaning dividend is at the minimum value,
    # and thereby the result will be at the maximum value, since dividing a negative value by -1
    # will result in a positive value.

    # Thereafter, I check if either the dividend or divisor is negative,
    # if so, I return the result of the division as a negative value.
    # Otherwise, I return the result of the division as a positive value.
