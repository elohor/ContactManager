class Contact:

	def __init__(self, name, phone_number, gender, email_address, postal_address):
		self.name = name
		self.phone_number = phone_number
		self.gender = gender
		self.email_address = email_address
		self.postal_address = postal_address

	def get_contact(self):
		print ("Name: {}\nNumber: {}\nGender: {}\nEmail: {}\nPostal: {}\n".format(
			self.name, self.phone_number, self.gender,
			self.email_address, self.postal_address)
		)


class ContactManager:
	def __init__(self, persons=[]):
		self.persons = persons

	def add_persons(self, contact):
		self.persons.append(contact)

	def delete_persons(self, name):
		for contact in self.persons:
			if name == contact.name:
				self.persons.remove(contact)
				return contact
			else:
				return "no name found"

	def search_persons(self, name):
		for contact in self.persons:
			if name == contact.name:
				return contact
			else:
				print ("There is no such name")

	def get_contacts(self):
		print ([contact.name for contact in self.persons])
		

	# def __repr__(self):
	# 	print ("name is :{}".format(','.join(self.get_con

if __name__ == "__main__":
	my_contact = ContactManager()
	my_contact.add_persons(Contact("elohor","2344", "f", "elohorthomas@yahoo.com", "345"))
	my_contact.add_persons(Contact("simon","23484", "m", "simon@yahoo.com", "3465"))
	# my_contact.delete_persons(Contact("elohor","2344", "f", "elohorthomas@yahoo.com", "345"))
	# my_contact.search_persons(Contact("elohor","2344", "f", "elohorthomas@yahoo.com", "345"))
	# my_contact.__repr__()
	my_contact.get_contacts()
