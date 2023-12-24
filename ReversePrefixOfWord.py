class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse_list = []
        i = word.find(ch)

        return word[:i+1][::-1] + word[i+1:]
