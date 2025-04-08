<<<<<<< HEAD

def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)

    remaining = goal - (max_big * 5)

=======

def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)

    remaining = goal - (max_big * 5)

>>>>>>> d2f3f40 (commit)
    return remaining if remaining <= small else -1