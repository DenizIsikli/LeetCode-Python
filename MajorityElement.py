class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0

        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res

    # Solving this with the two variables "count" and "res": "count" for how many times the number showed up
    # in the list, "res" for the current number we're on.
    # I then go through the given list and checks if "count" is equal to 0 which it should be on the first iteration
    # so I then add the first number to res, and if the same number appears another place in the list, "count" adds 1
    # to itself - which it does each time res is assigned to num, otherwise it subtracts 1 meaning the numbers
    # weren't similar.