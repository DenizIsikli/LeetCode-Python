class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums

    # For every index starting at 1
    # Add the current element to the previous element, creating a running sum
    # Return the list
