s = 'abcdefghijklmnopqrstuvwxyz'

print(s[1:3] == 'bc')
print(s[0:14] == 'abcdefghijklmn')
print(s[14:] == 'opqrstuvwxyz')
print(s[1:][:24] == 'bcdefghijklmnopqrstuvwxy')
