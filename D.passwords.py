d = {'anna', 'annA', 'anNa', 'anNA', 'aNna', 'aNnA', 'aNNa'}
tmp = {'aNNA', 'Anna', 'AnnA', 'AnNa', 'AnNA', 'ANna', 'ANnA', 'ANNa', 'ANNA'}
d.update(tmp)
dig = 0
upper = 0
lower = 0
notAnna = 1
s = input()
l = list(s)
unique_cnt = len(set(l))
for i in range(len(s)):
    if s[i].islower():
        lower = 1
    if s[i].isupper():
        upper = 1
    if s[i].isdigit():
        dig = 1
    if i < len(s)-3 and s[i:i+4] in d:
        notAnna = 0
if (len(s) > 7 and dig and upper and lower and notAnna and unique_cnt > 3):
    print('strong')
else:
    print('weak')
