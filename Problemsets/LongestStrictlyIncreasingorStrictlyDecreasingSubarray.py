class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1
        inc = [1] * n
        dec = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1
            if nums[i] < nums[i - 1]:
                dec[i] = dec[i - 1] + 1
        return max(max(inc), max(dec))

    # If not nums, return 0
    # If n is 1, return 1
    # Otherwise, initialize inc and dec to [1] * n
    # Iterate i over [1, n)
    # If the current element is greater than the previous element, increment inc[i] by inc[i - 1] + 1
    # Otherwise, if the current element is less than the previous element, increment dec[i] by dec[i - 1] + 1
    # Return the maximum of the maximum of inc and the maximum of dec
