# should_continue = True
# if should_continue == True:
# 	print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter ther person you know: ")

# if person in known_people:
# 	print("you know {}!".format(person))
# else:
# 	print("you don't know {}!".format(person))

## Excercise
def who_do_you_know():
	# Ask the user for the list of people they know
	person_list = input("Enter the names of people you know, separated by commas: ")
	# Split the string into a list
	person_without_spaces = [person.strip() for person in person_list.split(",")]
	# Return that list
	return person_without_spaces
def ask_user(person_list):
	# Ask user for a name
	name = input("Enter a name of someone you know: ")
	# See if their name is in the list of people they know
	if name in person_list:
		# Print out that they know the person
		print("You know {}".format(name))
	else:
		print("You don't know {}".format(name))

ask_user(who_do_you_know())