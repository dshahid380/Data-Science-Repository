def LCS(P, Q, n, m):
	"""It retunrs the maximum common subsequesnces"""
	if n == 0 or m == 0:
		result = 0

	elif P[n-1] == Q[m-1]:
		result = 1 + LCS(P, Q, n-1, m-1)

	elif P[n-1] != Q[n-1]:
		result = max(LCS(P, Q, n-1, m), LCS(P, Q, n, m-1))

	return result

#Test cases
"""INPUT
  1    
  4 5
  BATD
  ABACD"""

"""OUTPUT
  3"""

for _ in range(int(input())):
	N, M = map(int, input().split())
	P = input()
	Q = input()

	print(LCS(P, Q, N, M))

