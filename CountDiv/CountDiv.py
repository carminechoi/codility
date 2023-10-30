# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # Implement your solution here
    divisibleCount = 0

    for i in range(A, B+1):
        if i % K == 0:
            divisibleCount += 1
    
    return divisibleCount