class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedList = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != sortedList[i]:
                result+=1
        return result

    # Firstly I sort the given list to then iterate through the given list, and if "i" is not in the sorted list
    # it adds one to the "result" variable, showcasing how many indices don't match and at last returns the result
