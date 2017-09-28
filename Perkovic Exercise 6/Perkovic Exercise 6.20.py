phonebook = {'Smith, Jane': '123-45-67', 'Doe, John': '987-65-43', 'Baker,David': '567-89-01'}


def reverse(esrever):
    bookphone = {}
    for k, v in esrever.items():
        bookphone[v] = k
    return bookphone


print(reverse(phonebook))
    