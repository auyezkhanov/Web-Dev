<<<<<<< HEAD

def front_back(str):
  if len(str) < 2:
    return str
=======

def front_back(str):
  if len(str) < 2:
    return str
>>>>>>> d2f3f40 (commit)
  return str[-1] + str[1:-1] + str[0]