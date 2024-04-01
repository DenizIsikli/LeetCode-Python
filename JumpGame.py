class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jumps = 0
        for i in range(len(nums) - 1):
            max_jumps = nums[i] if nums[i] > max_jumps else max_jumps
            if max_jumps == 0:
                return False
            max_jumps -= 1
        return True

    # I set max_jumps to 0
    # I iterate through the array, updating max_jumps to the maximum of the current element and max_jumps
    # If max_jumps is 0, return False
    # Otherwise, decrement max_jumps
    # If the loop completes, return True
