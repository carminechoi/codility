# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    uniqueElements = set(A)
    sortedElements = sorted(uniqueElements)
    
    previous = 0
    for element in sortedElements:
        if element != previous + 1:
            return previous + 1
        previous += 1
    
    return previous + 1 if previous > 1 else 1