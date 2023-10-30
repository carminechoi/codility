# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)

    positive_set = set()

    for num in A:
        if num > 0:
            positive_set.add(num)

    for i in range(1, N + 2):
        if i not in positive_set:
            return i