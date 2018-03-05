try:
    while 1:
        s = input()
        print(s[:8], end='')
        s = s.split('\t')
        message = s[len(s)-1]
        cnt = 72-len(message)
        print('.'*cnt, end='')
        print(message, end='')
except:
    raise SystemExit
