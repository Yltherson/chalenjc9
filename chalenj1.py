
ip = input("Antre adres ip a: ")

pot = 0
for i in ip:
    if(i.isdigit()):
        pot += int(i)

print(pot)