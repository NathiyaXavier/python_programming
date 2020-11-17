'''
Function Description
Complete the circularArrayRotation function in the editor below. It should return an array of integers representing the values at the specified indices.

circularArrayRotation has the following parameter(s):
a: an array of integers to rotate
k: an integer, the rotation count
queries: an array of integers, the indices to report
Input Format
The first line contains  space-separated integers, , , and , the number of elements in the integer array, the rotation count and the number of queries.
The second line contains  space-separated integers, where each integer  describes array element  (where ).
Each of the  subsequent lines contains a single integer denoting , the index of the element to return from .
Output Format
For each query, print the value of the element at index  of the rotated array on a new line.

Sample Input 0
3 2 3
1 2 3
0
1
2
Sample Output 0

2
3
1
'''
# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    for i in range(k):
        temp = a[-1]
        for j in range(len(a)-1,0,-1):
            a[j] = a[j-1]
        a[0]=temp

    new_arr = []
    for i in queries:
        new_arr.append(a[i])

    return new_arr


if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print(result)

