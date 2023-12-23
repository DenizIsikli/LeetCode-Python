class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""

    # Going backwards from the end of the string: (Start, Stop, Step),
    # I check if the number is odd, if it is, I return the string up to that point,
    # otherwise I return an empty string
