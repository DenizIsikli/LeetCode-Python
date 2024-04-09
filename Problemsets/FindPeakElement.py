class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l

    # I initialize the left and right pointers to the start and end of the input list nums.
    # I then enter a while loop that continues until the left pointer is less than the right pointer.
    # I calculate the middle index of the list.
    # If the number at the middle index is greater than the number to its right,
    # I update the right pointer to the middle index, isolating left to mid.
    # Otherwise, I update the left pointer to mid+1, isolating right to mid.
    # I continue this process until the left pointer is equal to the right pointer.
    # Finally, I return the left pointer as the peak element.
