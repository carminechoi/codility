# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    permutation = set()
    length = len(A)

    for num in A:
        if num <= length:
            permutation.add(num)

    return 1 if len(permutation) == length else 0