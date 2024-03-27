class Solution:
    def toHex(self, num: int) -> str:
        return hex(num & 0xFFFFFFFF).replace('0x', '')

    # I use the hex() function to convert the number to hexadecimal.
    # I use the bitwise AND operator to convert negative numbers to positive numbers.
    # I use the replace() function to remove the '0x' prefix from the hexadecimal number.
    # I return the hexadecimal number as a string.
