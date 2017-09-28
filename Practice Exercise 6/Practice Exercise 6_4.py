studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    ans = []
    for student in studentencijfers:
        ans.append(sum(student) / len(student))
    return ans

def gemiddelde_van_alle_studenten(studentencijfers):
    return sum(gemiddelde_per_student(studentencijfers)) / len(studentencijfers)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))