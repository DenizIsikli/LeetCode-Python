class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                temp = 0

            if temp > cnt:
                cnt = temp
        return cnt

    # I set two variables to store the count of consecutive ones and the temporary count.
    # Then iterate through the list of numbers.
    # If the number is 1, increment the temporary count.
    # If the number is 0, reset the temporary count to 0.
    # Then compare the temporary count with the count of consecutive ones.
    # If the temporary count is greater, update the count of consecutive ones.
    # Finally, return the count of consecutive ones.
    