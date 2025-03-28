class mathmanager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b
	
	def interest(self, a, b):
			return a * (1.038^b)

	def taxPaid(self, income):
		if income < 12570:
			return 0
		elif 12570 < income < 50270:
			return income * 0.8
		elif 50370 < income < 125140:
			return income * 0.6
		else: 
			return income * 0.55

