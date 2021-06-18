# string formatting
name = "Ryan"
# Using the old .format() method:
print('His name is {var}.'.format(var=name))
# Using f-strings:
print(f'His name is {name}.')
# use different styles of quotation marks to avoid conflicts
d = {'a':123,'b':456}
print(f"Address: {d['a']} Main Street")
print()

# widths, alignmnet and padding
library = [
    ('Author', 'Topic', 'Pages'), 
    ('Twain', 'Rafting', 601), 
    ('Feynman', 'Physics', 95), 
    ('Hamilton', 'Mythology', 144)
    ]
# pass arguments inside a nested set of curly braces to set a minimum width for the field, 
# the alignment and even padding characters
# use the character < for left-align, ^ for center, > for right.
# to set padding, precede the alignment character with the padding character (- and . are common choices).
for author, topic, pages in library:
    print(f'{author:{10}} {topic:{10}} {pages:.>{7}}')
print()

# date formatting
from datetime import datetime
today = datetime(year=2018, month=1, day=27)
print(f'{today:%B %d, %Y}')
print()

# file operations
# check your notebook location, use pwd or cwd
import os
print(os.getcwd())
# opening a text file
text_file = open("test_files/test.txt")
# my_file is now an open file object held in memory.
print(text_file)
# reading and seeking a file
# reading
print(text_file.read())
# reading again
print(text_file.read())
# empty output because the "cursor" is at the 
# end of the file after having read it, we need to reset it.
text_file.seek(0)
# Now read again
print(text_file.read())
# readlines returns a list of lines in a file.
text_file.seek(0)
print(text_file.readlines())
# always do this when you're done with a file
text_file.close()  
print()
# writing to a file
# Opening a file with 'w' or 'w+' 
# truncates the original, meaning that anything 
# that was in the original file is deleted!
text_file = open("test_files/test.txt", "w+")
# writing
text_file.write('This is a new first line')
print()
# appending to a file
# 'a+' lets us read and write to a file. 
# If the file does not exist, one will be created.
text_file = open("test_files/test.txt", "a+")
text_file.write('\nThis line is being appended to test.txt')
text_file.write('\nAnd another line here.')
text_file.seek(0)
print(text_file.read())
print()
# we can assign temporary variable names as aliases, and 
# manage the opening and closing of files automatically 
# using a context manager
with open("test_files/test.txt","r") as txt:
    first_line = txt.readlines()[0]
    
print(first_line)
print()
# iterating through a file
with open("test_files/test.txt","r") as txt:
    for line in txt:
        # the end='' argument removes extra linebreaks
        print(line, end='')