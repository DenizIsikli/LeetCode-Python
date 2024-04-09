class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        else:
            return [-1, -1]
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                end = j
                break
        else:
            return [-1, -1]

        return [start, end]

    # I first check if the list is empty, if it is, I return [-1, -1]
    # Otherwise, I iterate through the list to find the first occurrence of the target and store the index in start
    # If I don't find it, I return [-1, -1]
    # I then iterate through the list in reverse to find the last occurrence of the target and store the index in end
    # If I don't find it, I return [-1, -1]
    # I return the start and end indices in a list
    # waht does the -1, -1, -1 mean?
