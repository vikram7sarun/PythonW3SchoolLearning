# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

filePath = "F:\PYTHON_AUTOMATION\PythonW3Schools\Data\demofile.txt"

# f = open(filePath,"rt")

# print(f.read())
# print(f.read(5))
# print(f.read(11))

# print(f.readline())
# print(f.readline())

# for x in f:
#   print(x)
#
# f.close()


# File Write

f = open(filePath,"w")
f.write("Woops! I have deleted the content!")
f.close()

# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("demofile.txt")

# Check if File exist:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Delete Folder
os.rmdir("myfolder")







