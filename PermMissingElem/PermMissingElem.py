# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    realSum = sum(A)
    maxSum = 0
    for i in range(1, len(A)+2):
        maxSum += i

    return maxSum - realSum