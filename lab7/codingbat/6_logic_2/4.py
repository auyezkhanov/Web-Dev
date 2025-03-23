<<<<<<< HEAD

def fix_teen(n):
  if n in range(13, 20):
    if n == 15 or n == 16:
      return n
    return 0
  return n

def no_teen_sum(a, b, c):
=======

def fix_teen(n):
  if n in range(13, 20):
    if n == 15 or n == 16:
      return n
    return 0
  return n

def no_teen_sum(a, b, c):
>>>>>>> d2f3f40 (commit)
  return sum(map(fix_teen, (a,b,c)))