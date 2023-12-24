class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

    # With the use of a hashset, I iterate through the given list and check whether "i" is in the hashset - if it is,
    # it's duplicated and returns True, otherwise it adds the number to the hashset and at last returns false once done
