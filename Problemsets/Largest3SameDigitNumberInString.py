class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i] > largest:
                    largest = num[i]

        return largest * 3 if largest else ""

    # I go through the string and check if the current digit is the same as the next two digits,
    # if so, I check if it is larger than the current largest and if so, I update the largest,
    # otherwise, I return the largest * 3, otherwise, I return an empty string if there are no 3 consecutive digits.
