<<<<<<< HEAD
def repeatedString(s, n):
    full_repeats = n // len(s)
    remainder = n % len(s)
    
    return s.count('a') * full_repeats + s[:remainder].count('a')

# Test cases
print(repeatedString("aba", 10))   # Output: 7
print(repeatedString("a", 100000)) # Output: 100000
print(repeatedString("abc", 7))    # Output: 3
=======
def repeatedString(s, n):
    full_repeats = n // len(s)
    remainder = n % len(s)
    
    return s.count('a') * full_repeats + s[:remainder].count('a')

# Test cases
print(repeatedString("aba", 10))   # Output: 7
print(repeatedString("a", 100000)) # Output: 100000
print(repeatedString("abc", 7))    # Output: 3
>>>>>>> d2f3f40 (commit)
