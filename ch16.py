import string

p = print
car = input("antre mo a :\n")

mo = car.split()
a = string.ascii_uppercase

for i in mo:
    if(i[0]==">"):
        l = a.index(i[2])+int(i[1])
        p(a[l], end="")
    elif(i[0]=="<"):
        l = a.index(i[2])-int(i[1])
        p(a[l], end="")
