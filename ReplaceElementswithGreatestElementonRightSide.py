class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

    # I assign "rightMax" in the beginning since the last value of
    # the list will be -1.

    # Then I iterate through the list in a reversed order
    # and assign "newMax" to the biggest value between "rightMax"
    # and "arr[i]"/current value with the "max()" function

    # I then assign the "arr[i]"/current value to "rigthMax" and
    # assign "rightMax" to newMax, placing the bigger value to the
    # side, so I can iterate through the rest of the list without
    # "newMax"