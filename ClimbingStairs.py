class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]

    # I first check if the input is less than or equal to 2. If so, return n.
    # Then I create a dp list with the first two elements being 1 and 2.
    # I then loop from 2 to n and append the sum of the previous two elements to the dp list.
    # Finally, I return the last element of the dp list, which is the highest combination.
