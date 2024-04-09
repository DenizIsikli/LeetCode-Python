class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        for op in operations:
            if op[1] == '+':
                res += 1
            else:
                res -= 1

        return res

    # I set res to 0
    # I iterate through the operations list
    # If the second character of the operation is '+', I increment res by 1
    # Otherwise, I decrement res by 1
    # I return res
