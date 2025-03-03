with open ('D:\Code2\Lab6\ex.txt','r') as f:
    l=f.readlines()
with open('D:\Code2\Lab6\ex2.txt','a') as f:
    for i in l:
        f.write(i)