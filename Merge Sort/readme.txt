The problem of sorting a list of numbers lends itself immediately to a divide-and-conquer strategy: split the list into two halves, recursively sort each half, and then merge the two sorted sublists (recall the problem “Merge Two Sorted Arrays”).

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A[1..n].

Sample Dataset
10
20 19 35 -18 17 -20 20 1 4 4
Sample Output
-20 -18 1 4 4 17 19 20 20 35
