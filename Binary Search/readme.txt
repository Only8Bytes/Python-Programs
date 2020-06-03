The problem is to find a given set of keys in a given array.

Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

Sample Dataset
5
6
10 20 30 40 50
40 10 35 15 40 20
Sample Output
4 1 -1 -1 4 2
