class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(x) for x in str(num)])
        return num

    # While num is greater or equal to 10, sum the digits of num
    # Return the sum of the digits of num
