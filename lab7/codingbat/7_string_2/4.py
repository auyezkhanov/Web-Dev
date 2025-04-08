<<<<<<< HEAD

def count_code(str):
  count = 0
  for i in range(len(str) - 3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
      
=======

def count_code(str):
  count = 0
  for i in range(len(str) - 3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
      
>>>>>>> d2f3f40 (commit)
  return count