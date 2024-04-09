class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i+len(needle)]:
                return i

        return -1

    # I first check if the needle is an empty string. If it is, I return 0.
    # Then I check if the needle is longer than the haystack. If it is, I return -1.

    # Then I loop through the haystack, and check if the needle is equal to the substring of the haystack
    # from i to i + len(needle), meaning I check if the letters equal to the len of the needle are equal to the needle.
    # If it is, I return i, else I return -1.
