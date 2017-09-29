def easyCrypto(str):
    newStr = ''
    for char in str:
        if ord(char) % 2 == 0:
            newStr += chr(ord(char) - 1)
        else:
            newStr += chr(ord(char) + 1)
    return newStr

print(easyCrypto('abc'))
print(easyCrypto('ZOO'))