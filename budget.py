class Category :

	def __init__(self, type_cat) :
		self.budget_cat = type_cat
		self.ledger = []
		self.budget_tot = 0

		#print('Created objet',  self.budget_cat)

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

#-------------------------------------------------------------------------------
def create_spend_chart(list_cat) :
	exp_tot = 0
	exp_dict = {}
	chart_dict = {}
	max_length = 0
	for bCat in list_cat :
		withdrawal = 0
		for (amnt,desc) in bCat.ledger :
			if amnt < 0 and 'Transfer' not in desc :
				withdrawal += abs(amnt)
				exp_tot += abs(amnt)
		exp_dict[bCat.budget_cat] = withdrawal
		if len(bCat.budget_cat) > max_length :
			max_length = len(bCat.budget_cat)
	
	for bCat, exp in exp_dict.items() :
		chart_dict[bCat] = round(100 * exp/exp_tot)

	expenditure = 'Percentage spent by category\n'
	percentage = reversed(range(0, 110, 10))
	for n in percentage :
		ratio_to_show = ''
		horiz_line = '    ' 
		for v in chart_dict.values() :
			if v >= n :
				ratio_to_show += ' o '
			elif (n - v) <= 5 :
				ratio_to_show += ' o '
			else :
				ratio_to_show += '   '
			horiz_line += '---' 

		expenditure = expenditure + str(n).rjust(3) + '|' + ratio_to_show + '\n'
	horiz_line += '-' 
	expenditure += horiz_line + '\n'


	cat_name = ''
	for char in range(0, max_length) :
		cat_name += '    '
		for cat in chart_dict.keys() :
			if char < len(cat) :
				cat_name += cat[char].center(3)
			else :
				cat_name += '   '
		cat_name += '\n'
	expenditure += cat_name


	return expenditure


