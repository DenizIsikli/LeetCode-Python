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
