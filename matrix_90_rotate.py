""" 
Given an n x n matrix, rotate it 90 degrees clockwise in place.
Input: A 2D list matrix
Output: The rotated matrix
Example
 
Input
>>> rotate([[1,2,3],[4,5,6],[7,8,9]])
[[7,4,1],[8,5,2],[9,6,3]]

>>> rotate([[5, 1, 9,11],[2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]])
[[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]]
"""


def rotate(matrix: list) -> list:
    n = len(matrix)

    # Transpose (troca linhas por colunas)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse cada linha
    for row in matrix:
        row.reverse()

    return matrix


if __name__ == "__main__":
    from doctest import testmod
    testmod()
