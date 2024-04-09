class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        return x_str == x_str[::-1]

    # I first check if the input is negative. If so, return False.
    # Then I convert the integer to a string and check if it is equal to its reverse.
    # If so, return True. Otherwise, return False.
    