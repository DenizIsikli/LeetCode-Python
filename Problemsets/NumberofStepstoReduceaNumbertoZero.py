class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps

    # I set steps to 0
    # While num is greater than 0
    # If num is divisible by 2, divide num by 2
    # Else subtract 1 from num
    # Increment steps by 1
    # Return steps
