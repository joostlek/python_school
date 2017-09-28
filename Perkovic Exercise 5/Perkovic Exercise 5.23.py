def pay(wage, hours):
    if hours > 60:
        return 40 * wage + 20 * wage * 1.5 + (hours - 60) * wage * 2
    elif hours > 40:
        return 40 * wage + (hours - 40) * wage * 1.5
    else:
        return hours * wage

print(pay(10, 35))
print(pay(10, 45))
print(pay(10, 61))
