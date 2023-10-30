# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # Implement your solution here
    count = B // K - (A - 1) // K
    
    return count