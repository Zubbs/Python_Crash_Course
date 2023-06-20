# the first step in working with a text file is to read the text file to memory.

with open('pi_digits.txt') as file_object:  # you initially need a open() to access a file. 'With' closes the file once access is not needed
    contents = file_object.read()  # reads the entire contents of the file when an object has been created for python
    print(contents) # in the output, read() returns an empty string when it reaches the end of the file, which shows up as a blank line
                    # you can remove that balnk line with contents.rstrip() which will remove whitespace characters from the right of the string 



# file paths 
# sometimes the file you might want to work with won't be in the same directory, just provide the file path in open()
# these fiel paths could be absolute/relative

file_path = '/Users/nzube/Desktop/code_/Python_Crash_Course/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)


# reading files line by line - use for loops in the file_object 
# also doing this line by line adds new line characters after each line of the file

# using the with block limits processing of the file to that block, to save the file to a list for later processing use .readlines()

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


#Replacing strings, you can use .replace() 

for line in lines:
    y = line.replace('x','y') # word to replace, #replacement


#Writing to a File

filename = 'programing.txt'

with open(filename, 'w') as file_object: # other modes you can open to a file, read ('r), append ('a'), read&write (r+)
    file_object.write('I love programming') # if the file does not exist, python will create the file but can overwrite existing files


# you would have to format your strings using \n and \t 

