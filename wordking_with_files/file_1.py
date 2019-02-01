"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = [1, 2, 3]

my_file = open("firstfile1.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()
