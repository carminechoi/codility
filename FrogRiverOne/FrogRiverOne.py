# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    positions = set()
    
    for time, leaf_position in enumerate(A):
        positions.add(leaf_position)
        
        if len(positions) == X:
            return time

    return -1