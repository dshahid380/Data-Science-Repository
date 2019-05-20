def knapsack(n, C, W, v):
	if n == 0 or C == 0:
		result = 0

	elif W[n-1] > C:
		result = knapsack(n-1, C, W, v)

	else:
		result = max(knapsack(n-1, C, W, v), v[n-1] + knapsack(n-1, C-W[n-1], W, v))
	return result


#Test case
"""INPUT
1
5 10
2 3 5 4 2
7 4 2 1 5
"""
"""OUTPUT
   16
"""

for _ in range(int(input())):
	N, C = map(int, input().split())
	W = [int(x) for x in input().split()]
	v = [int(x) for x in input().split()]
	print(knapsack(N, C, W, v))

