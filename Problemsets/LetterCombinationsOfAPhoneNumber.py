class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []

        def dfs(i, path):
            if i == len(digits):
                res.append(path)
                return
            for letter in digit_to_letters[digits[i]]:
                dfs(i+1, path+letter)

        dfs(0, '')
        return res

    # I first check if the input is empty. If so, just return an empty list.
    # Then I create a dictionary that maps each digit to the corresponding letters.

    # I recursively call the dfs function with the index of the current digit and the current path.
    # If the index is equal to the length of the digits string, then we have a complete combination,
    # so we add it to the res list and return.
