import os
path=os.getcwd()
os.chdir('D:\Code2\Lab5')
l=os.listdir()
for i in l:
    if os.path.isfile(i): # isdir for directories
        print(i)