class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

    # I first find the transpose of the matrix by swapping the elements across the diagonal,
    # basically x, y coordinates in a regular graph
    # I then reverse each row of the matrix
    # This rotates the matrix by 90 degrees
