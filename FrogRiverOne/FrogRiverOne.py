# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    
    for i in range(len(A)):
        if A[i] >= X:
            return i

    return -1