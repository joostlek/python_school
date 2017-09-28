def exclamation(s):
    txt = []
    for char in s:
        txt += char
    vowels = 'AEIOUaeiou'
    res = ''
    for char in txt:
        if char in vowels:
            char *= 5
        res += char
    return res + '!'

print(exclamation("lmako"))
