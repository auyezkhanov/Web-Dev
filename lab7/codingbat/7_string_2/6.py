<<<<<<< HEAD

def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i:i+3] == 'xyz':
      if i > 0 and str[i - 1] == '.':
        continue
      else:
        return True
  
=======

def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i:i+3] == 'xyz':
      if i > 0 and str[i - 1] == '.':
        continue
      else:
        return True
  
>>>>>>> d2f3f40 (commit)
  return False