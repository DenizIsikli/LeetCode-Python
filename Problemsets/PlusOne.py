class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        if digits[-1] == 9:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])

        return digits

    # I first check if the length of the digits is 1 and if the first digit is 9. If it is, I return [1, 0].
    # Then I check if the last digit is not 9. If it is not, I add 1 to the last digit and return digits.

    # Then I check if the last digit is 9. If it is,
    # I set the last digit to 0 and call the function again on the digits without the last digit recursively.
