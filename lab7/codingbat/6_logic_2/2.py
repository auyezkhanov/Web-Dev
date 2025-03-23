<<<<<<< HEAD
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c:
    sum += a
  if b != c and b != a:
    sum += b
  if c != a and c != b:
    sum += c
=======
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c:
    sum += a
  if b != c and b != a:
    sum += b
  if c != a and c != b:
    sum += c
>>>>>>> d2f3f40 (commit)
  return sum