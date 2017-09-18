class Contact:


	def __init__(self, name, phone_number, gender, email_address, postal_address):
		self.name = name
		self.phone_number = phone_number
		self.gender = gender
		self.email_address = email_address
		self.postal_address = postal_address

	def get_contact(self):
		print ("Name: {}\n Number: {}\n Gender: {}\n Email: {}\n Postal: {}\n".format(
			self.name, self.phone_number, self.gender,
			self.email_address, self.postal_address)
		)

name = input("Enter name:")
phone_number = input("Enter phone number:")
gender = input("Enter gender:")
email_address = input("Enter email:")
postal_address = input("Enter Postal Address:")

newContact = Contact(name, phone_number, gender, email_address, postal_address)

newContact.get_contact()


