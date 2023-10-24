# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    minimumDifference = remainingSum = sum(A)
    rollingSum = 0

    for num in A:
        rollingSum += num
        remainingSum -= num
        minimumDifference = min(minimumDifference, abs(remainingSum - rollingSum))

    return minimumDifference