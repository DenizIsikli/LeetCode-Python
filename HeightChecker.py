class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedList = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != sortedList[i]:
                result+=1
        return result