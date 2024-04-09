class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange-1
            numExchange += 1
            count += 1
        return count

    # Set count to numBottles
    # While numBottles >= numExchange
    # Subtract numExchange-1 from numBottles, since we can exchange numExchange bottles for 1 bottle
    # Increment numExchange, since we have exchanged numExchange bottles
    # Increment count, since we have drunk 1 bottle
    # Return count
