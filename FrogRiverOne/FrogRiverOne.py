# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    length = len(A)

    for i in range(length):
        if A[i] >= X:
            return i

    return length