def indexes(s, f):
    res = []
    for i in range(len(s)):
        if s[i] in f:
            res.append(i)
    return res

print(indexes('mississippi', 's'))