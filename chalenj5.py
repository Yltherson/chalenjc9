chenn = "5 45 123 12"
print("chenn : ",chenn)

lis = chenn.split(" ")

p = 1

for el in lis:
    s = 0
    for i in range(len(el)):
        s = s + int(el[i])

    p *=s

print("Rezilta : ",p)