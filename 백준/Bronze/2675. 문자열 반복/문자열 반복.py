N = int(input())
for i in range(N):
	ilst = input().split()
	R = int(ilst[0])
	for elem in ilst[1]:
		print(elem*R, end='')
	print()