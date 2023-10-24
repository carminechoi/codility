# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    counts = {}
    for num in A:
        counts[num] = counts.get(num, 0) + 1
    
    for key, value in counts.items():
        if value == 1:
            return key

    # time: O(2n) -> O(n)
    # space: O(n)