class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

    # I join an empty string with the reversed list of words in the input string s.
