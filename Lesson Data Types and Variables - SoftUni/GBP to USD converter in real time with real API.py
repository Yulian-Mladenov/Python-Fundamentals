# This is the original example of the teacher:
# import requests
#
# amount = int(input('Enter an amount of pounds: '))
#
# response = requests.get('https://api.exchangerate-api.com/v4/latest/GBP')
# exchange_rate = response.json()['rates']
# usd_rate = exchange_rate['USD']
# usd_amount = amount * usd_rate
#
# us_dollars = usd_amount
#
# print(f'{amount:.2f} GBP is equivalent to {us_dollars:.2f} USD')


# This is second example of the teacher:
import requests

choice = input('Choice currency: \n1. USD \n2. GBP \n3.JPY \nPlease,select your choice: ')

if choice == '1':
    amount = int(input('Please input your amount: '))
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    exchange_rate = response.json()['rates']
    usd_rate = exchange_rate['USD']
    usd_amount = amount * usd_rate
    us_dollars = usd_amount

elif choice == '2':
    amount = int(input('Please input your amount: '))
    response = requests.get('https://api.exchangerate-api.com/v4/latest/GBP')
    exchange_rate = response.json()['rates']
    usd_rate = exchange_rate['USD']
    usd_amount = amount * usd_rate
    us_dollars = usd_amount

elif choice == '3':
    amount = int(input('Please input your amount: '))
    response = requests.get('https://api.exchangerate-api.com/v4/latest/JPY')
    exchange_rate = response.json()['rates']
    usd_rate = exchange_rate['USD']
    usd_amount = amount * usd_rate
    us_dollars = usd_amount

print(f'{amount:.2f} GBP is equivalent to {us_dollars:.2f} USD')
