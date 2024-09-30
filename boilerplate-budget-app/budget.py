class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def transfer(self, ammount, category):
    sucessful = self.withdraw(ammount, "Transfer to " + category.name)
    if sucessful:
      category.deposit(ammount, "Transfer from " + self.name)
      return True
    return False

  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction["amount"]
    return balance

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}\n"
      total += item['amount']
    output = title + items + "Total: " + str(total)
    return output


def create_spend_chart(categories):
  print_str = "Percentage spent by category\n"
  total_spent = 0
  spent_by_category = []
  for category in categories:
    spent = 0
    for item in category.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
    spent_by_category.append(spent)
    total_spent += spent

  percentages = []
  for spent in spent_by_category:
    percentage = int(spent / total_spent * 100)
    percentages.append(percentage)

  for i in range(100, -1, -10):
    print_str += f"{i:3}|"
    for percentage in percentages:
      if percentage >= i:
        print_str += " o "
      else:
        print_str += "   "
    print_str += " \n"

  print_str += "    " + "-" * (len(categories) * 3 + 1) + "\n"
  max_length = max(len(category.name) for category in categories)
  for i in range(max_length):
    print_str += "    "
    for category in categories:
      if i < len(category.name):
        print_str += " " + category.name[i] + " "
      else:
        print_str += "   "
    print_str += " \n"

  print_str = print_str.rstrip() + "  "
  print(print_str)
  return print_str
