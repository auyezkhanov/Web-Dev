<<<<<<< HEAD
def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return leap

year = int(input())
=======
def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return leap

year = int(input())
>>>>>>> d2f3f40 (commit)
print(is_leap(year))