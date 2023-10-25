# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    counters = [0] * N
    maxCount = 0
    lastMaxCount = 0

    for num in A:
        if num >= N + 1:
            lastMaxCount = maxCount
        else:
            if counters[num-1] < lastMaxCount:
                counters[num-1] = lastMaxCount
            counters[num-1] += 1
            maxCount = max(maxCount, counters[num-1])

    for i in range(N):
        if counters[i] < lastMaxCount:
            counters[i] = lastMaxCount

    return counters