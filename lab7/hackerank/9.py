<<<<<<< HEAD
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum(1 for apple in apples if s <= a + apple <= t)
    orange_count = sum(1 for orange in oranges if s <= b + orange <= t)

    print(apple_count)
    print(orange_count)

# Test cases
countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])  
# Output:
# 1
# 1

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])  
# Output:
# 1
# 2
=======
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum(1 for apple in apples if s <= a + apple <= t)
    orange_count = sum(1 for orange in oranges if s <= b + orange <= t)

    print(apple_count)
    print(orange_count)

# Test cases
countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])  
# Output:
# 1
# 1

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])  
# Output:
# 1
# 2
>>>>>>> d2f3f40 (commit)
