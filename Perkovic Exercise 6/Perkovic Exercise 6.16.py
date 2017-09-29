str = ''
for i in range(ord('a'), ord('z') + 1):
    str += '{0}:{1:02X} '.format(chr(i), i).lower()
    if i == ord('m'):
        str += '\n'
print(str)