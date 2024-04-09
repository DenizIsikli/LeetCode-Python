class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        coordinates = {(x, y)}

        for i in path:
            if i == "N": y += 1
            elif i == "S": y -= 1
            elif i == "E": x += 1
            elif i == "W": x -= 1
            if (x, y) in coordinates: return True
            coordinates.add((x, y))

        return False

    # Starting at (0, 0), we go through each character in the path and move accordingly,
    # then I check if the coordinates are in the set, if it is, I return True meaning it has looped itself,
    # otherwise I return False meaning it hasn't looped itself
