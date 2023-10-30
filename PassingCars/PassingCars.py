# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    eastCount = 0
    pairs = 0

    for car in A:
        if car == 0:
           eastCount += 1
        else:
            pairs += eastCount
            
            if pairs > 1000000000:
                return -1

    return pairs