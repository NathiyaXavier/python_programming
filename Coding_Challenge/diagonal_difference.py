# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(len(arr)):
        j = i
        primary_diagonal += arr[i][j]

    for i in range(len(arr)):
        j = len(arr) - 1 -i
        secondary_diagonal += arr[i][j]
    return abs(primary_diagonal-secondary_diagonal)


if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
