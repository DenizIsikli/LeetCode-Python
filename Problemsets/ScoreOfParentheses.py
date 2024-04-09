class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    score += 1 << depth

        return score

    # I go through the string and check if the current digit is '(', if so, I increment the depth,
    # otherwise, I decrement the depth and check if the previous digit is '(',
    # if so, I increment the score by 2 ** depth.
    # Finally, I return the score.
