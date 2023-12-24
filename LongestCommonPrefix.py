class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        output = ""
        firstWord = strs[0]

        for c in range(len(firstWord)):
            for word in strs:
                if c == len(word) or word[c] != firstWord[c]:
                    return output
            output += strs[0][c]

        return output
