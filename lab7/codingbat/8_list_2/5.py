<<<<<<< HEAD

def sum67(nums):
  flag = False
  sum = 0
  for i in range(len(nums)):
    if flag:
      if nums[i] == 7:
        flag = False
      continue
    
    if nums[i] == 6:
      flag = True
      continue
      
    sum += nums[i]
  
=======

def sum67(nums):
  flag = False
  sum = 0
  for i in range(len(nums)):
    if flag:
      if nums[i] == 7:
        flag = False
      continue
    
    if nums[i] == 6:
      flag = True
      continue
      
    sum += nums[i]
  
>>>>>>> d2f3f40 (commit)
  return sum