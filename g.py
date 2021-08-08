"""
You can split an integer N into two non-empty parts by cutting it between any pair of consecutive digits. After such a cut, a pair of integers A, B is created.

Your task is to find the smallest possible absolute difference between A and B in any such pair. If integer B contains leading zeros, ignore them when calculating the difference.

For example, the number N = 12001 can be split into:

A = 1 and B = 2001. Their absolute difference is equal to |1 − 2001| = 2000.

A = 12 and B = 001. Their absolute difference is equal to |12 − 1| = 11.

A = 120 and B = 01. Their absolute difference is equal to |120 − 1| = 119.

A = 1200 and B = 1. Their absolute difference is equal to |1200 − 1| = 1199.

In this case, the minimum absolute difference is equal to |12 − 1| = 11 for A = 12 and B = 001.

Write a function:



class Solution { public int solution(int N); }



that, given an integer N, returns the smallest possible absolute difference of any split of N.

Examples:

1. Given N = 12001, your function should return 11, as explained above.

2. Given N = 510, your function should return 5. The possible splits are:

A = 5 and B = 10, with the absolute difference equal to |5 − 10| = 5,

A = 51 and B = 0, with the absolute difference equal to |51 − 0| = 51.

The smallest possible absolute difference is 5.

3. Given N = 7007, your function should return 0. The smallest absolute difference can be achieved by splitting N into A = 7, B = 007.

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

Assume that:

N is an integer within the range [10..1,000,000,000].
"""
