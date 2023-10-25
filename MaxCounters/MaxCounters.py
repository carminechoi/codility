# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    counters = [0] * N
    maxCount = 0

    for num in A:
        if num >= N + 1:
            counters = [maxCount] * N
        else:
            counters[num-1] += 1
            maxCount = max(maxCount, counters[num-1])

    return counters