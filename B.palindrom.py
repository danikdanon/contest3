def single_centre(centre, s):
    d = 1
    ans = 1
    max_d = min(len(s)-centre-1, centre)
    while d <= max_d:
        if s[centre-d] != s[centre+d]:
            ans = 0
        d += 1
    if ans:
        return max(centre, len(s)-centre-1) - max_d
    else:
        return 10000

def double_centre(centre, s):
    d = 1
    ans = 1
    max_d = min(len(s) - centre - 2, centre)
    while d <= max_d:
        if s[centre-d] != s[centre+d+1]:
            ans = 0
        d += 1
    if ans:
        return max(centre, len(s)-centre-2)-max_d
    else:
        return 10000

s = input()
ans = len(s)-1

for centre in range(len(s)):
    ans = min(ans,single_centre(centre, s))
    if centre < len(s) - 1 and s[centre] == s[centre+1]:
        ans = min(ans, double_centre(centre, s))

print(ans)
