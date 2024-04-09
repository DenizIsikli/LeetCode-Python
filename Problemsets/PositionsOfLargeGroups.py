class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start = 0
        for i in range(len(s)):
            if i == len(s) - 1 or s[i] != s[i + 1]:
                if i - start + 1 >= 3:
                    res.append([start, i])
                start = i + 1
        return res

    # I create a new list to store the result, and use two pointers to record the start and end of each group.
    # If the length of a group is larger than or equal to 3, I append it to the result list.
    # If it isn't, I move the start pointer to the next index to start a new group.
    # Lastly, I return the result list.
