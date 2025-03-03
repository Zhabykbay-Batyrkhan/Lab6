import os

path='D:\Code2\Lab5'

def f(path):
    if os.path.exists(path):
        print(f"{path} exists")

        d = os.path.dirname(path)
        print(f"{d} is a directory portion")

        f_n = os.path.basename(path)
        print(f"{f_n} is a filename")
    else:
        print("The file does not exist")

f(path)
