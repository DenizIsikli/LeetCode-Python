class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            left, right = 0, num/2

            while left <= right:
                mid = (left+right)//2
                x = mid * mid
                if x == num:
                    return mid
                elif x > num:
                    right = mid - 1
                else:
                    left = mid + 1

    # If num is 1, return True
    # Otherwise, set left to 0 and right to num/2
    # While left is less than or equal to right, set mid to the average of left and right
    # Set x to mid squared
    # If x is equal to num, return mid
    # If x is greater than num, set right to mid - 1
    # If x is less than num, set left to mid + 1
