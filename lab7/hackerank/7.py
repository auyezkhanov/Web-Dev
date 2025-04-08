<<<<<<< HEAD
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps

# Test cases
print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))  # Output: 3
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))    # Output: 3
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # Output: 4
=======
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps

# Test cases
print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))  # Output: 3
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))    # Output: 3
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # Output: 4
>>>>>>> d2f3f40 (commit)
