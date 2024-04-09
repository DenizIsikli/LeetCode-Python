class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1, max2 = 0, 0

        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)

        return (max1 - 1) * (max2 - 1)

    # I find the two largest numbers in the list and return the product of the two largest numbers minus 1.
