<<<<<<< HEAD
def make_bricks(small, big, goal):
  
  max_big = min(big, goal // 5)  
  
  remaining = goal - (max_big * 5)
  
=======
def make_bricks(small, big, goal):
  
  max_big = min(big, goal // 5)  
  
  remaining = goal - (max_big * 5)
  
>>>>>>> d2f3f40 (commit)
  return remaining <= small