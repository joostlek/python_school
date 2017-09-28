def ticker(filename):
    file = open(filename)
    res = {}
    comp = file.readlines()
    file.close()
    for company in comp:
        tick = company.split(':')[1]
        compa = company.split(':')[0]
        res[tick] = compa
    return res

companies = ticker('ticker.txt')
company = input('Enter Company name: ')
for k, v in companies.items():
    if v == company:
        print('Ticker Symbol: {0}'.format(k))
ticke = input('Enter Ticker symbol: ')
print('Company name: {0}'.format(companies[ticke + '\n']))