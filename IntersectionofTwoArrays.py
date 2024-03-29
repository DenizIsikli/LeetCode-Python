class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    # I return the intersection of the two lists by converting them to sets and using the & operator,
    # which returns the intersection of the two sets (common elements).
    # I convert the result back to a list and return it.
