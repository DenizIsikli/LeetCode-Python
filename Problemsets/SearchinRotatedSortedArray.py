class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # I first check if the input is empty. If so, just return -1.
    # I then set the left and right pointers to the start and end of the input list.
    # I then set the mid-pointer to the middle of the list.

    # I then check if the mid-pointer is equal to the target. If so, return the mid-pointer.
    # I then check if the left pointer is less than or equal to the mid-pointer.
    # If so, I check if the target is between the left and mid-pointers.
    # If so, I set the right pointer to the mid - 1, meaning I move the right pointer to the left of the mid-pointer,
    # enclosing the target.

    # If not, I move the left pointer to the right of the mid-pointer, enclosing the target.
    # If the left pointer is greater than the mid-pointer, I check if the target is between the mid and right pointers.
    # If so, I move the left pointer to the right of the mid-pointer, enclosing the target.
    # If not, I move the right pointer to the left of the mid-pointer, enclosing the target.
    # If the target is not found, return -1.
