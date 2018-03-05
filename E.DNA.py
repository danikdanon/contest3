s = input()
d = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
ls = list(s)
n = len(ls)
for i in range(n):
    ls[i] = d[ls[i]]

for i in range(n):
    print(ls[n-1-i], end='')
