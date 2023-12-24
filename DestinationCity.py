class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        destinations = {cityB for cityA, cityB in paths}

        for cityA, cityB in paths:
            destinations.discard(cityA)

        return destinations.pop()

    # I create a set of all the destination cities.
    # Then, I go through the paths and remove the cityA from the set.
    # Finally, I return the only city left in the set, which is the destination city.
