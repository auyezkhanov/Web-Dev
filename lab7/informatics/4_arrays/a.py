<<<<<<< HEAD
n = int(input())
array = list(map(int, input().split()))

=======
n = int(input())
array = list(map(int, input().split()))

>>>>>>> d2f3f40 (commit)
print(*[array[i] for i in range(len(array)) if i % 2 == 0], sep=" ")