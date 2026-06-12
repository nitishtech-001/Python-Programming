class  Atm:
	# constructor call when the object initaly created
	def __init__(self):
		self.pin = None
		self.balance = 0
		
	# display the menu like atm simulation
	def menu(self):
		user_input = input("""
			Hello, how would you like to procces?
			1. Enter 1 to create/update pin
			2. Enter 2 to deposite
			3. Enter 3 to windraw
			4. Enter 4 to check balance
			5. Enter 5 to  exit
		""")
		ispin_generated = False if self.pin is None else True
		if not ispin_generated :
			print("Generate pin first... \n")
			self.create_pin()
			return self.menu()

		if not self.validate_user():
			print("Thank you for using atm...\n")
			return

		match user_input:
			case "1":
				self.create_pin()
			case "2":
				self.deposite()
			case "3":
				self.withdraw()
			case "4":
				self.check_balance()
			case "5":
				print("Thank you... Have a nice day.")
			case _:
				print("Wrong input choose correct one\n\n")
				self.menu()

    # varifing the user pin is correct or not max 3 attempt
	def validate_user(self,count=0):
		if count == 2:
			print("Max attempt card block for 24 Hour...\n")
			return False
		user_pin = input("Enter the pin : ")
		if not user_pin or user_pin != self.pin:
			return self.validate_user(count+1)
		return True

    # creating pin of new user or updating
	def create_pin(self):
		pin = input("Enter the 4 digit pin  : ")
	
		if not pin or len(pin) > 4:
			print("Wrong pin input again....")
			return self.create_pin()
		# now set that pin of that user
		self.pin = pin
		print("Pin generated successfully.\n")

    # adding the amount to the account
	def deposite(self):
		# add money to the account
		money = input("Enter the amount : ")
		if not money or not money.isDigit():
			print("Enter the correct amount...")
			return self.deposite()

		self.deposite += float(money)
		print("Despite successfully.\n")

    # removing the money form the account
	def withdraw(self):
		money = input("Enter the amount : ")
		if not money and not money.isDigit():
			print("Enter the correct amount...")
			return self.withdraw()
		money = float(money)
		# now validate that it correct amoutn or not
		if money > self.balance:
			print("Insufficient balance..")
			return
		self.balance -= money
		print("Withdrawal successfully.\n")

	# display the balance
	def check_balance(self):
		print(f"Current Balance :::: {self.balance} \n")

if __name__ == "__main__":
	customer1 = Atm()
	customer1.deposite(10000)
	customer1.check_balance()
	customer1.withdraw(5000)

    