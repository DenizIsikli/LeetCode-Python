class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

    # I return True if the length of s is equal to the length of goal,
    # and goal is a substring of s + s.
