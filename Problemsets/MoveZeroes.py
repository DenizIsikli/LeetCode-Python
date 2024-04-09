class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

    # I go through the list and if I find a zero, I remove it and append it to the end of the list.
