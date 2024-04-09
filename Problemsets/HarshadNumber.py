class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x % sum([int(i) for i in str(x)]) == 0:
            return sum([int(i) for i in str(x)])
        else:
            return -1

    # If x is divisible by the sum of the digits of x
    # Return the sum of the digits of x
    # Otherwise return -1
