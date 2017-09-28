def inBoth(lst1, lst2):
    for item in lst1:
        if item in lst2:
            return True
    return False

print(inBoth([3, 2, 5, 4, 7], [9, 0, 1, 3]))
