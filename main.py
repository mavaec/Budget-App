from budget import Category, create_spend_chart

bFood = Category('food')
bClothing = Category('clothing')
bEnter = Category('entertaintment')


bFood.deposit(500.0, 'Initial deposit of 0af')
bFood.deposit(30.259999, 'Refund')
bFood.withdraw(10.00, 'Wine')
bFood.withdraw(50, 'Groceries')

bFood.transfer(100, bClothing)
bClothing.withdraw(60, 'Pants')
bClothing.withdraw(20, 'Socks')

bEnter.deposit(250, 'Initial deposit')
bEnter.withdraw(85, 'Theater')

print(bFood.get_balance())
print(bClothing.get_balance())
print(bEnter.get_balance())

print(create_spend_chart([bFood, bClothing, bEnter]))