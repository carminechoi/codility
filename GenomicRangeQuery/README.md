
# GenomicRangeQuery

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

A DNA sequence can be represented as a string consisting of the letters <tt style="white-space:pre-wrap">A</tt>, <tt style="white-space:pre-wrap">C</tt>, <tt style="white-space:pre-wrap">G</tt> and <tt style="white-space:pre-wrap">T</tt>, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an <i>impact factor</i>, which is an integer. Nucleotides of types <tt style="white-space:pre-wrap">A</tt>, <tt style="white-space:pre-wrap">C</tt>, <tt style="white-space:pre-wrap">G</tt> and <tt style="white-space:pre-wrap">T</tt> have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?
The DNA sequence is given as a non-empty string S = <tt style="white-space:pre-wrap">S[0]S[1]...S[N-1]</tt> consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K &lt; M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).
For example, consider string S = <tt style="white-space:pre-wrap">CAGCCTA</tt> and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:
<ul style="margin: 10px;padding: 0px;"><li>The part of the DNA between positions 2 and 4 contains nucleotides <tt style="white-space:pre-wrap">G</tt> and <tt style="white-space:pre-wrap">C</tt> (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.</li>
<li>The part between positions 5 and 5 contains a single nucleotide <tt style="white-space:pre-wrap">T</tt>, whose impact factor is 4, so the answer is 4.</li>
<li>The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide <tt style="white-space:pre-wrap">A</tt> whose impact factor is 1, so the answer is 1.</li>
</ul>

Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(S, P, Q)</tt></p>
that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.
Result array should be returned as an array of integers.
For example, given the string S = <tt style="white-space:pre-wrap">CAGCCTA</tt> and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">100,000</span>];</li>
<li>M is an integer within the range [<span class="number">1</span>..<span class="number">50,000</span>];</li>
<li>each element of arrays P and Q is an integer within the range [<span class="number">0</span>..<span class="number"><tt style="white-space:pre-wrap">N - 1</tt></span>];</li>
<li>P[K] ≤ Q[K], where 0 ≤ K &lt; M;</li>
<li>string S consists only of upper-case English letters <tt style="white-space:pre-wrap">A, C, G, T</tt>.</li>
</ul>


