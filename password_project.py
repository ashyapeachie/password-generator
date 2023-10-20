import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "<>,.;:=+-_!@*$#/"

upper, lower, numbers, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numbers:
    all += digits
if syms:
    all += symbols

length = 15
amount = 5

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

    
