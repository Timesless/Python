from typing import List


def rotate_matrix(matrix: List[List[int]]) -> None:
    """
    N * N 矩阵表示图像，每个像素大小为4字节，请顺时针旋转图像90°
    :param matrix: 参数矩阵
    :return:
    """
    matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
    for row in matrix:
        row.reverse()
    print(matrix)


mx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_matrix(mx)


