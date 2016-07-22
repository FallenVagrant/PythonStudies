#Make a set out of a sequence
X = set("spam")

#Make another set with set literals
Y = {'h', 'a', 'm'}

#A tuple of 2 sets without parentheses (Unordered)
print("X and Y set contents:",X, Y)

#Intersection - Same characters
print("Intersecting characters:", X & Y)

#Union
print("Union:", X | Y)

#Difference
print("Difference:", X - Y)

#Filter out duplicates
print("1, 2, 1, 3, 1 without duplicates:", list(set([1, 2, 1, 3, 1])))

#Check existence of something in sets
print("'p' is in set 'spam':", 'p' in set("spam"))