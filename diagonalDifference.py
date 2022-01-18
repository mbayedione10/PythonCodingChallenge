def diagonalDifference():
    """
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    :return: int: the absolute diagonal difference
    """
    n = int(input("The number of rows and columns in the square matrix"))
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(i, j)
            arr[i][j] = float(input("arr[{}][{}]= ".format(i, j)))
    left_diag = 0
    right_diag = 0
    i = 0
    j = 0
    k = n - 1
    while i < n:
        if arr[i][j] == arr[j][i]:
            left_diag = left_diag + arr[i][j]
        right_diag = right_diag + arr[i][k]
        i = i + 1
        j = j + 1
        k = k - 1
    if right_diag > left_diag:
        diff = right_diag - left_diag
    else:
        diff = left_diag - right_diag
    return int(diff)


if __name__ == '__main__':
    print(diagonalDifference())