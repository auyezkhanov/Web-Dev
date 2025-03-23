<<<<<<< HEAD
def sockMerchant(n, ar):
    from collections import Counter
    sock_counts = Counter(ar)
    return sum(count // 2 for count in sock_counts.values())

# Test cases
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Output: 3
print(sockMerchant(4, [1, 1, 3, 3]))                          # Output: 2
print(sockMerchant(5, [1, 2, 3, 4, 5]))                       # Output: 0
=======
def sockMerchant(n, ar):
    from collections import Counter
    sock_counts = Counter(ar)
    return sum(count // 2 for count in sock_counts.values())

# Test cases
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Output: 3
print(sockMerchant(4, [1, 1, 3, 3]))                          # Output: 2
print(sockMerchant(5, [1, 2, 3, 4, 5]))                       # Output: 0
>>>>>>> d2f3f40 (commit)
