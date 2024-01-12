class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0] * (len(nums)+1)
        for num in nums:
            count[num] += 1

        duplicate = count.index(2)
        missing = count.index(0, 1)
        return [duplicate, missing]

    # I create a list of 0s with the length of nums + 1.
    # I iterate through nums and increment the count by 1 for each number.
    # I find the index of the duplicate number and the missing number.
    # I return the duplicate and missing numbers.
