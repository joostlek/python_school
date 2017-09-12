klinkers = 'aeiou'
s = "Guido van Rossum heeft programmeertaal Python bedacht."
for char in s:
    if char in klinkers:
        print(char)
