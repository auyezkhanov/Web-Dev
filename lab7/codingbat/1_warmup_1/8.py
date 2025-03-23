<<<<<<< HEAD

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  
=======

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  
>>>>>>> d2f3f40 (commit)
  return a < 0 and b > 0 or a > 0 and b < 0