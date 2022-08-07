a = int(input("Antre prmye nonb la :\n"))
b = int(input("Antre dezyem nonb la :\n"))

n = 20

miltipA = []
miltipB = []
mAB = []
notAB = []


for i in range(n+1):
    if(i%a == 0):
        miltipA.append(i)

    if(i%b == 0):
        miltipB.append(i)

    if((i%a !=0) and (i%b !=0)):
        notAB.append(i)

for i in range(n+1):
    if(i in miltipA and i in miltipB):
        mAB.append(i)

print("\n")

for el in miltipA:
    print(el, end=" ")
print("-->",len(miltipA))
print("\n")

for el in miltipB:
    print(el, end=" ")
print("-->",len(miltipB))
print("\n")

for el in mAB:
    print(el, end=" ")
print("-->",len(mAB))
print("\n")

for el in notAB:
    print(el, end=" ")
print("-->",len(notAB))

