class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    # I join every word in each array into a single string and compare them.
    # If they are equal, the function will return True, otherwise False.
