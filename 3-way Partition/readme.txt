Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.

Sample Dataset
9
4 5 6 4 1 2 5 7 4
Sample Output
2 1 4 4 4 5 7 6 5
