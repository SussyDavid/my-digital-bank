import datetime
from sqlite3 import Timestamp

class Account:
    auto_account_number = 1234567890
    
    def __init__(self, currency: str, initial_balance: float = 0):
        self.account_number = Account.auto_account_number
        Account.auto_account_number += 1
        self.currency = currency
        self.initial_balance = initial_balance
        self.timestamp = datetime.datetime.now()
    @property
    def account_number(self):
        return self.account_number

    
class Trans:
    def __init__(self, amount: float = 0, note: str = " "):
        self.amount = amount
        self.note = note
        self.timestamp = datetime.datetime.now()           

class Client:
    clients = []
    def __init__(self, name: str):
        self.name = name
        self.timestamp = datetime.datetime.now()
        self.accounts = []
        Client.clients.append(self)

    def add_account(self, account: Account):
        self.accounts.append(account)
    


    def print_accounts(self):
        for account in self.accounts:
            print(f"Account of client {self.name}")
            print(f'{account.account_number} ({account.currency} {account.initial_balance})')
#Izveido komandā funkciju/metodi (add_account), kas pievienos klietam kontu

Clients = []

Clients.append(Client("Bobs Bobiks Bobinsons III"))
Clients.append(Client("Anna 2"))
Clients[0].add_account(Account("EUR", 200))
Clients[1].add_account(Account("USD", 261))


c1 = Client('Anna')
#print(f'{c1.name} {c1.timestamp}')

c2 = Client('Jenifer')
#print(f'{c2.name} {c2.timestamp}')

#Account
#auto_account_number (automaticly assigned starting from 1234567890)
#currency: str (teksta datu tips: 'EUR', 'PLN', 'USD')
#initial_balance: float (decimala datu tips: 100.54, 458.63)
#timestamp



a1 = Account('EUR')
#print(a1.account_number)
a2 = Account('USD')
#print(a2.account_number)
a3 = Account('JPY')
#print(a3.account_number)
c2.add_account(Account("USD", 999))
c1.add_account(Account("USD", 69))
c1.add_account(Account("EUR", 21))
c1.add_account(Account("EUR", 420))

Clients[1].accounts[0].account_number = '999999999999'

for client in Client.clients:
    client.print_accounts()
