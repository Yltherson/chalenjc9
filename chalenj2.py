antye = input("antre yon nonb \n")

if(antye.isdigit()):
    if((float(antye)%4) != 0):
        print("OK")
    else:
        print("NOK")

else:
    print("ou pa antre yon nonb")