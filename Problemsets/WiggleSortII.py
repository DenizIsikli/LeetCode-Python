class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        # Sort the list
        # Find the middle index of the list
        # Reverse the first half and second half of the list
        # Assign the reversed halves to the list
        # The list is now sorted in the wiggle sort manner
