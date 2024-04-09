class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, list):
            res.append(list[:])
            for i in range(start, len(nums)):
                list.append(nums[i])
                backtrack(i + 1, list)
                list.pop()

        backtrack(0, [])
        return res

    # I set res to an empty list
    # I defined a helper function backtrack that takes in two arguments start and list
    # I appended the i'th element from nums to the list
    # I then recursively called the backtrack function with the updated list
    # I then pop the last element from the list
    # I then call the backtrack function with an empty list and 0 as the start index
    # I return the res list
