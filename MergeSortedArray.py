class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

        # I replace the elements from index m to the end of the list with the elements of nums2.
        # Thereafter, I sort the list.
