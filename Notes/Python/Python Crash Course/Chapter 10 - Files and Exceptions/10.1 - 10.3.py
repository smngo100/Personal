# 10-1. Learning Python
from pathlib import Path

path = Path('learning_python.txt')

# Prints the contents once by reading in the entire file
contents = path.read_text()
print(contents)
print()

# Stores the lines in a list and then loops over each line
lines = contents.splitlines()
for line in lines:
    print(line)
print()

# 10-2. Learning C
new_contents = contents.replace('Python', 'C')
print(new_contents)
print()

# 10-3. Simpler Code
# This section uses a temporary variable, lines, to show how splitlines() work.
# You can skip the temporary variable and loop directly over the list that splitlines() returns.

for line in contents.splitlines():
    print(line)
