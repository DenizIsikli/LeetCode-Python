class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #split() splits the string into pieces on every space
        split = s.split()

        return len(split[-1])

    # I use the split() function to split the string into pieces on every space, so I at last can return the
    # length of the last word