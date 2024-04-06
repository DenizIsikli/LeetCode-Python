class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

    # Set n to the length of nums
    # Initialize dp to a list of n elements, all set to 1
    # For i in the range from 1 to n
    # If the current element is not equal to the previous element
    # Set the current element in dp to the previous element in dp plus 1
    # Return the sum of dp, which is the number of alternating subarrays
