class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2
        ans = 0
        if nums[mid] < k:
            for i in range(mid, n):
                if nums[i] < k:
                    ans += k - nums[i]
                else:
                    break
        elif nums[mid] > k:
            for i in range(mid, -1, -1):
                if nums[i] > k:
                    ans += nums[i] - k
                else:
                    break
        return ans

    # Initialize n to the length of nums
    # Sort nums, so I can use binary search to find the median
    # Initialize mid to n // 2
    # Initialize ans to 0
    # If the median is less than k, iterate i over [mid, n), meaning the right half of the array
    # If the current element is less than k, increment ans by k - nums[i]
    # Otherwise, break
    # If the median is greater than k, iterate i over [mid, -1, -1), meaning the left half of the array
    # If the current element is greater than k, increment ans by nums[i] - k
    # Otherwise, break
    # Return ans
