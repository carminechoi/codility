# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # Implement your solution here

    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    result = []
    N = len(P)

    for i in range(N):
        left = P[i]
        right = Q[i]

        minimalImpact = 4
        for j in range(left, right + 1):
            minimalImpact = min(minimalImpact, impact[S[j]])
        result.append(minimalImpact)

    return result