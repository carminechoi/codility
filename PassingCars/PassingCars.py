# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    westCount = 0
    pairs = 0

    for car in A[::-1]:
        if car == 0:
           pairs += westCount
        else:
            westCount += 1

    return pairs