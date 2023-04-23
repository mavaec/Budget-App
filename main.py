from budget import Category, create_spend_chart

bFood = Category('food')
bClothing = Category('clothing')



bFood.deposit(1200.0, 'Initial deposit of 0abcdef')
bFood.deposit(30.259999, 'Refund')
bFood.withdraw(10, 'Wine')
bFood.withdraw(50, 'Groceries')

bFood.transfer(500, bClothing)
bClothing.withdraw(10, 'Pants')

print(bFood.get_balance())
print(bClothing.get_balance())
#print(bFood.check_funds(10))

print(create_spend_chart([bFood, bClothing]))