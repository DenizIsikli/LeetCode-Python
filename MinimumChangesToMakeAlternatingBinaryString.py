class Solution:
    def minOperations(self, s: str) -> int:
        operations_01 = 0
        operations_10 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    operations_01 += 1
                else:
                    operations_10 += 1
            else:
                if s[i] == "0":
                    operations_01 += 1
                else:
                    operations_10 += 1

        return min(operations_01, operations_10)

    # I go through the string and check if the current index is even or odd,
    # if even, I check if the current digit is 1, if so, I increment the operations_01,
    # otherwise, I increment the operations_10.
    # Otherwise, if the current index is odd, I check if the current digit is 0, if so, I increment the operations_01,
    # otherwise, I increment the operations_10.
    # Finally, I return the minimum of the operations_01 and operations_10.
