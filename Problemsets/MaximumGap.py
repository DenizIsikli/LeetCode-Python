class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        gap = 0
        for i in range(len(nums)-1):
            temp = nums[i] - nums[i+1]
            temp = abs(temp)
            gap = max(gap, temp)

        return gap

    # If the length of the list is less than 2, return 0
    # Otherwise, sort the list
    # Initialize the gap to 0
    # Iterate through the list
    # Calculate the difference between the current element and the next element
    # Take the absolute value of the difference, making it positive
    # Update the gap to the maximum of the current gap and the difference
    # Return the gap
