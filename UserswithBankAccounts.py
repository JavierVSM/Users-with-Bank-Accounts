class BankAccount:
  def __init__(self, accountNum, user):
    self.accountNum = accountNum
    self.user = user
    self.int_rate = 0.05
    self.balance = 0
    
  def deposit(self, amount):
    self.balance += amount
    print ("Your deposit was succeed. You have $", self.balance, "in your account")
    return self
      
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print ("Your withdrawal was succeed. You have $", self.balance, "in your account")
      return self
    else:
      print( "Insufficient funds: Charging a $5 fee." )
      self.balance -= 5
      return self

  def yield_interest(self):
    if self.balance >= 0:
      self.interest = self.balance * self.int_rate
      self.balance = self.balance + self.interest
      return self
  
  def display_account_info(self):
    print ("Your balance: $", self.balance)
    return self
    
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = BankAccount
    
  def make_deposit(self, BankAccount, amount):
    self.account = BankAccount
    self.account.deposit(amount)
    return self
  
  def make_withdrawal(self, BankAccount, amount):
    self.account = BankAccount
    self.account.withdraw(amount)
    return self
  
  def display_user_balance(self, BankAccount):
    self.account = BankAccount
    print( f"Owner: {self.name}\nAccount number: {BankAccount.accountNum}\nBalance: {BankAccount.balance}" )

carlos=User ("Carlos Mora", "mora@gmail.com")
laura=User ("Laura Cerdas", "lcerdas@gmail.com")

A001 = BankAccount(9090, carlos)
A002 = BankAccount(3333, carlos)
A003 = BankAccount(4444, laura)
A004 = BankAccount(3030, laura)

print ("Multiple accounts test:")
print (" ")
carlos.make_deposit(A001, 2000)
carlos.make_withdrawal(A001, 200)
carlos.display_user_balance(A001)
print (" ")
carlos.make_deposit(A002, 1000)
carlos.make_withdrawal(A002, 300)
carlos.display_user_balance(A002)
print (" ")
laura.make_deposit(A003, 20)
laura.make_withdrawal(A003, 50)
laura.display_user_balance(A003)
print (" ")
laura.make_deposit(A004, 100)
laura.make_withdrawal(A004, 50)
laura.display_user_balance(A004)