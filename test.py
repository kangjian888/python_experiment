def discribe(username):
	print("I am " + username.title())

discribe('KANGJIAN')

def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name_new(first_name, last_name, middle_name = ' '):
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

programmer = get_formatted_name_new('Jian', 'KANG', 'Alex')
print(programmer)

def build_person(first_name, last_name):
	person = {'first':first_name, 'last':last_name}
	return person

singer = build_person('Enying', 'YAN')
print(singer)


data = [1,2,3,4]
data_1 = data[:-1]
print(data)
print(data_1)