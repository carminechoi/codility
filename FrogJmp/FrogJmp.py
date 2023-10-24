# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    distanceToJump = Y - X
    jumps = -(distanceToJump // -D)

    return jumps