# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    sortedElements = sorted(A)
    
    previous = 0
    for element in sortedElements:
        if element > 0:
            if element == previous:
                continue
            elif element == previous + 1:
                previous += 1
            else:
                return previous + 1
    
    return previous + 1 if previous >= 1 else 1