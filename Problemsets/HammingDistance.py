class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

    # I calculate the XOR of the two numbers and convert it to binary.
    # Then count the number of 1s in the binary representation.
    # Finally, return the count of 1s.

    # XOR table
    # X | Y | X^Y
    # 0 | 0 | 0
    # 0 | 1 | 1
    # 1 | 0 | 1
    # 1 | 1 | 0
