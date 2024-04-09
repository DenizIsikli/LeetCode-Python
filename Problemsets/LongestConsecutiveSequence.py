class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        max_len = 0


        for num in nums:
            if num - 1 not in nums:
                curr_len = 1
                while num + 1 in nums:
                    num += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len

    # I first check if the input is empty. If so, just return 0.
    # Then I convert the input list to a set for faster lookup, since the list might contain duplicates.
    # I initialize the max_len variable to 0, to count the length of the longest consecutive sequence.
    # I iterate through the set of numbers, and for each number, I check if the previous number is not in the set,
    # which means that this is the start of a new consecutive sequence.
    # I then increment the num variable and curr_len variable
    # until the next number of the current number is not in the set.
    # I update the max_len variable with the maximum of the current length and the max_len.
    # Finally, I return the max_len variable.
