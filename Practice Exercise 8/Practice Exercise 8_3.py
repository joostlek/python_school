def code(str):
    newStr = ''
    for char in str:
        newStr += chr(ord(char) + 3)
    return newStr

print(code("RutteAlkmaarDen Helder"))