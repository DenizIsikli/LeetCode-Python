class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l

    # I assign the variable "l" to count the left overs of integers that are not duplicated.

    # I then iterate through the given list from 1 to the length of the list, instead of 0, since the first
    # element won't ever be duplicated.

    # And if the current number is not the same as the previous one in the list, assign "num[l]" to "num[r]" and
    # increment "l".

    # Lastly I return "l"