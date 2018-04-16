# Author: Henry Roberts
# 4/16/2018

class studentDining(object):
	# A Student at JMU who has punches, dining, and FLEX in an account.

	#	Attributes:
	#		Name: Their name.
	#		Punch Balance: How many punches they have left.
	#		Dining Balance: How much money they have left in dining dollars.
	#		FLEX Balance: How much money they have left in FLEX.

	name = 'temp'
	punchBalance = 123
	punchBalanceMax = 123
	diningBalance = 123
	flexBalance = 123

	def __init__(self, name, punch_balance, punch_balance_max, dining_balance, flex_balance):
		# The students name
		self.name = name
		self.punchBalance = punch_balance
		self.punchBalanceMax = punch_balance_max
		self.diningBalance = dining_balance
		self.flexBalance = flex_balance

	def set_punch_balance(self, balance):
		# Sets how many punches the student has.
		if balance > self.punchBalanceMax:
			self.punchBalance = self.punchBalanceMax
		else:
			self.punchBalance = balance

	def set_dining_balance(self, balance):
		# Sets how much money the student has in their dining account. 
		self.diningBalance = balance

	def set_flex_balance(self, balance):
		# Sets how much money the student has in their flex account.
		self.flexBalance = balance

	def withdraw_punch(self, punches):
		# Withdraws *punches* amount of punches. Fails if not enough 
		# punches in balance. 
		if punches > self.punchBalance:
			raise RuntimeError('Amount greater than available balance.')
		self.punchBalance -= punches
		return self.punchBalance

	def withdraw_dining(self, amount):
		# Withdraws *amount* amount of money from dining. Fails if not enough 
		# dining in balance. 
		if amount > self.diningBalance:
			raise RuntimeError('Amount greater than available balance.')
		self.diningBalance -= amount
		return self.diningBalance

	def withdraw_flex(self, amount):
		# Withdraws *amount* amount of money from flex. Fails if not enough 
		# flex in balance. 
		if amount > self.flexBalance:
			raise RuntimeError('Amount greater than available balance.')
		self.flexBalance -= amount
		return self.flexBalance

	def deposit_punches(self, punches):
		# Deposits more punches into the account. 
		self.punchBalance += punches
		return self.punchBalance

	def deposit_dining(self, amount):
		# Deposits more dining into the account. 
		self.diningBalance += amount
		return self.diningBalance

	def deposit_flex(self, amount):
		# Deposits more flex into the account. 
		self.flexBalance += amount
		return self.flexBalance

	def get_punch(self):
		# Returns the amount of remaning punches. 
		print self.punchBalance
		return self.punchBalance

	def get_dining(self):
		# Returns the amount of remaining dining. 
		print self.diningBalance
		return self.diningBalance

	def get_flex(self):
		# Returns the amount of remaning flex.
		print self.flexBalance 
		return self.flexBalance

	def get_name(self):
		# Returns students name. 
		print self.name 
		return self.name


# Created a student called Orlando
orlando = studentDining('Orlando', 14, 14, 250, 50)

# For loop that goes through his typical week
for x in range(0, 6):
		orlando.withdraw_punch(2)
		orlando.withdraw_dining(10)
		orlando.withdraw_flex(4)

# Tests Depositing
orlando.deposit_flex(35)
orlando.deposit_dining(70)

# Checks getters and if the amounts have changed
print 'Amounts'
orlando.get_punch()
orlando.get_dining()
orlando.get_flex()

# Tests setting over max punches,
# print statement is so able to track in console
print 'Setting punches over max'
orlando.set_punch_balance(500)
orlando.get_punch()

# Prints students name
print 'Students Name'
orlando.get_name()
