import random

code = input("encripting code Enter --> ")

# hash maker code
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_alpha = alpha.lower()
num = "1234567890"
sine = "@!#$%&*^?.,'`~"

length = len(code)
all =  alpha+num+sine+_alpha
incode = ''.join(random.sample(all, length))
#hash created
print("your hash is --> "+incode)

decode = input('Enter a code --> ')

if (incode == decode):
    print("code is --> "+code)
else:
    print('code not mached ?')
