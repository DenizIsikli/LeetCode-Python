class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for i in range(0, len(s), 2*k):
            s_list[i:i+k] = reversed(s_list[i:i+k])

        return "".join(s_list)

    # I create a list from the string.
    # I iterate through the list in steps of 2*k.
    # I reverse the slice of the list from i to i+k.
    # I return the list as a string.
