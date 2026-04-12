# Climbing Stairs (DP)

n = 5
a, b = 1, 1

for _ in range(n):
    a, b = b, a + b

print(a)
