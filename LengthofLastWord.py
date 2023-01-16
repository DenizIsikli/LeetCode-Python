class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val = 0

        #split() splits the string into piece on every space
        split = s.split()

        return len(split[-1])