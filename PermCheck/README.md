
# PermCheck

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green)

A non-empty array A consisting of N integers is given.
A <i>permutation</i> is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(A)</tt></p>
that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.
Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">1</span>..<span class="number">1,000,000,000</span>].</li>
</ul>


