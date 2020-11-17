'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''
# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    max_val = 0
    first_iteration = True

    for i in range(len(arr)):
        val = 0
        for index,data in enumerate(arr,0):
            if(index!=i):
                val += data
        if first_iteration:
            mini_val = val
            first_iteration = False
        if val<mini_val:
            mini_val = val
        if val>max_val:
            max_val=val

    print(mini_val,max_val)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)