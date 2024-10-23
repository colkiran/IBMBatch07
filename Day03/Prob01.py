
# accept a number and display the no of times each digit is occurring
# 32409823482

from collections import  Counter
st = "324098234822222233333"

print(Counter(st))


#----------------------------------------------------

name = "MADAM"
j=len(name)-1
for i in range(0,len(name)):
    if i<=j:
        if name[i]==name[j]:
            palin = True
        else:
            palin = False
            break

if palin == True:
    print(f"String {name} is palindrom")
else:
    print(f"String {name} is not palindrom")
