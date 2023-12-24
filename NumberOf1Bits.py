class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bits = 0
        n_list = list(bin(n))

        for i in range(len(n_list)):
            if n_list[i] == '1':
                one_bits += 1

        return one_bits

    # I convert the number to binary and convert the binary number to a list.
    # I go through the list and check if the current digit is 1, if so, I increment the one_bits.
    # Finally, I return the one_bits.
    