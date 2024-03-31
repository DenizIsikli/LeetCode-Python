class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == len(nums):
                output.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        output = []
        backtrack(0)
        return output

    # I define a helper function called backtrack that takes in a parameter first
    # If first is equal to the length of nums, meaning I have reached the end of the list
    # I then append a copy of the list to the output list
    # Otherwise, I iterate through the list starting at the first index
    # I swap the first element with the current element
    # I recursively call backtrack with first incremented by 1
    # I swap the elements back to their original positions, because I want to explore all possible permutations
    # I initialize an empty list called output
    # I call backtrack with first set to 0
    # I return the output list
