class Solution:
    def findComplement(self, num: int) -> int:
        complement = bin(num)[2:]
        res = ''
        for binary in complement:
            if binary == '1':
                binary = '0'
            else:
                binary = '1'
            res += binary

        return int(res, 2)
