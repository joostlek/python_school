from math import floor
lst = [1, 5, 6, 7, 9, 3, 1]
if len(lst) % 2 == 0:
    mid = int(len(lst) / 2)
else:
    mid = floor(len(lst) / 2)
print(lst[mid:mid+1])
lst.sort(reverse=True)
lst.append(lst[0])
lst.pop(0)
print(lst)
