class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return (num + t) + t

    # Return the sum of num and t, then add t to the sum
