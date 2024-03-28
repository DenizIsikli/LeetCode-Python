class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []

        for word in words:
            for row in rows:
                if all([c.lower() in row for c in word]):
                    res.append(word)
                    break
        return res

    # I firstly set all the rows in a list.
    # Then iterate through the words and rows to check if all the characters in the word are in the row.
    # If so, append the word to the result list.
    # Finally, return the result list.
