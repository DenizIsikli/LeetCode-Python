class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)): nums.remove(val)
        return len(nums)

    # I go through the list and remove all instances of val using count() and remove().
    # Then I return the length of the list.
