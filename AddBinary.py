class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # Firstly I convert the binary strings into integers and add them together,
    # then I convert the sum back into binary form and return everything after the '0b' part,
    # since bin() returns a prefix '0b'.
