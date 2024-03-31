class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

    # Return if the sorted target list is equal to the sorted arr list
    