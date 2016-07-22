#Create one dictionary entry
bread = {'name': 'Bread', 'type': 'Granary', 'quantity': 5}

#Retrieve the dictionary values
print("Food name:", bread['name'])
print(bread['name'], "type:", bread['type'])
print(bread['type'], bread['name'], "quantity: ", bread['quantity'])

#Change dictionary Value
print("Adding 5 to the quantity...")
bread['quantity'] += 5
print("New quantity:", bread['quantity'])

#Create custom dictionary entry
D = {}
D['name'] = input("\n\nPlease type your name: ")
D['job'] = input("Please type your job title: ")
D['age'] = input("Please type in your age: ")

print("Thank you, your details are:")
print("Name:", D['name'], " | Job Title:", D['job'], " | Age:", D['age'])

#Another way to create a dictionary
bob1 = dict(name="Bob", job="Developer", age=40)
print(bob1['name'], "is a", bob1['age'], "year old", bob1['job'], ".")

#Dictionary with nesting
rec = {'name': {'first': 'John', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40}
print("\n\nJohn's surname:", rec['name']['last'])
print("John's first job:", rec['jobs'][0])
print("John's most recent job:", rec['jobs'][-1])
#Add another job
rec['jobs'].append('Janitor')
print("John's new job:", rec['jobs'][-1])
