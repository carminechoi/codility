# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    minimumDifference = float('inf')
    remainingSum = sum(A)
    rollingSum = 0

    for num in A[:-1]:
        rollingSum += num
        remainingSum -= num
        difference = abs(rollingSum - remainingSum)
        minimumDifference = min(minimumDifference, difference)

    return minimumDifference