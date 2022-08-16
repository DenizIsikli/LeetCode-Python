class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return -1

    # Sort nums
    # Iterate through nums from 1 to len(nums)
    # If nums[i] == nums[i - 1], return nums[i]
    # Return -1 if no duplicate found
