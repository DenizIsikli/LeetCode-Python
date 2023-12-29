class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        return word[:i+1][::-1] + word[i+1:]

    # I find the index of ch in word.
    # I return the reversed slice of word from the start to the index of ch.
    # I return the concatenation of the reversed slice and the rest of word.
