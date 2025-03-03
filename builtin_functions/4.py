import time

s = int(input("Square root of: "))
time_s = int(input("After miliseconds: "))

r = s**(1/2)

time.sleep(time_s/1000)

print(f"Square root of {s} after {time_s} miliseconds is {r}")