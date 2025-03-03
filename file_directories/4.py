with open(r'D:\Code2\Lab6\ex2.txt', 'r') as f:
    l = f.readlines()

    l = [line.strip() for line in l if line.strip()]
    print(len(l))  
