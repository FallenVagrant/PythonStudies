#Create a new file in output mode ('w' is write)
#Also, set the Unicode encoding to be safe
f = open('Test.txt', 'w', encoding='utf-8')

#Write strings to the file
f.write("Hello")
f.write(" World!")

#Close the file to flush output buffers to disk
f.close() 

#Open the file in read mode ('r', which is default)
#Also, set the Unicode encoding to be safe
r = open('Test.txt', encoding='utf-8')

#Read entire file into a string and print
t = r.read()
print(t)
r.close()

#Prompt for file path, read contents and print
inPath = input("Please type the path of the file you want to access:")
file = open(inPath, encoding='utf-8')
print("File path is:", inPath)
read = file.read()
print(read)
file.close()


#Prompt for file path and print contents, line-by-line, using a for loop
inPath2 = input("Please type another path of a file you want to access:")
for line in open(inPath2, encoding='utf-8'):print(line)
