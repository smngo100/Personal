##### Reading the Contents of a File #####
"""
* Path: The exact location of a file or folder on a system.
* Library: A module that provides specific functionality.
"""
# This opens the file, reads it, and prints the contents of the file
from pathlib import Path 

path = Path('pi_digits.txt') 
contents = path.read_text()
print(contents) 


##### Relative and Absolute File Paths #####
"""TWO MAIN WAYS TO SPECIFY PATHS IN PROGRAMMING"""
# 1) Relative file path: Tells Python to look for a given location relative to the director where the currently running program file is stored. 
path = Path('text_files/filename.txt')

# 2) Absolute file path: Tell Python exactly where the file is on your computer, regardless of where the programm that's being executed is stored.
# These paths are usually longer than realtive paths, because they start at your system's root folder 
path = Path('/home/user/data_files/text_files/filename.txt')


##### Accesing a File's Lines ##### 
# splitlines() method turns a long string into a set of lines
from pathlib import Path 

path = Path('pi_digits.txt') 
contents = path.read_text() 
lines = contents.splitlines()
for line in lines: 
  print(line) 


##### Working with a File's Contents ##### 
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))






