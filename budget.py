class Category :

	#budget_cat = ('food', 'clothing', 'entertainment')
	# self.budget_cat = None
	# self.ledger = []
	# self.budget_tot = 0

	def __init__(self, type_cat) :
		#print('Object created')
		# if type in self.budget_cat :
		# 	print('It is')
		# else :
		# 	print('NOT a valid category')
		self.budget_cat = type_cat
		self.ledger = []
		self.budget_tot = 0

		print('Created objet',  self.budget_cat)

	def deposit(self, amnt, desc) :
		self.ledger.append((amnt, desc))
		self.budget_tot += amnt
		#print(self.budget_cat)


	def withdraw(self, amnt, desc) :
		if self.check_funds(amnt) == True :
			self.ledger.append((-amnt, desc))
			self.budget_tot -= amnt
			return True
		else :
			return False


	def get_balance(self) :
		# print(self.budget_cat.center(30, '*'))
		# for (amnt,desc) in self.ledger :
		# 	amnt_decimals = "{0:.2f}".format(amnt)
		# 	len_amnt = len(amnt_decimals)
		# 	len_desc = len(desc)
		# 	print(desc[0:23].ljust(23,' ') + str(amnt_decimals)[-7:].rjust(7, ' '))
		# print('Total:', "{0:.2f}".format(self.budget_tot))

		balance = ''
		balance = balance + self.budget_cat.center(30, '*') + '\n'
		for (amnt,desc) in self.ledger :
			amnt_decimals = "{0:.2f}".format(amnt)
			len_amnt = len(amnt_decimals)
			len_desc = len(desc)
			balance = balance + desc[0:23].ljust(23,' ') + str(amnt_decimals)[-7:].rjust(7, ' ') + '\n'
		balance = balance + 'Total: ' + "{0:.2f}".format(self.budget_tot) + '\n'

		return balance




	def transfer(self, amnt, bCat) :
		if self.check_funds(amnt) == True :
			self.withdraw(amnt, 'Transfer to ' + bCat.budget_cat)
			bCat.deposit(amnt, 'Transfer from ' + self.budget_cat)
			return True
		else :
			return False


	def check_funds(self, amnt) :
		if amnt < self.budget_tot :
			return True
		else :
			return False

def create_spend_chart(list_cat) :
	expenditure = 'Percentage spent by category\n'
	tot_exp = 0
	chart_dict = {}
	for bCat in list_cat :
		withdrawal = 0
		for (amnt,desc) in bCat.ledger :
			if amnt < 0 and 'Transfer' not in desc :
				withdrawal += abs(amnt)
				tot_exp += abs(amnt)
		chart_dict[bCat.budget_cat] = withdrawal

		print(chart_dict)


	return expenditure


