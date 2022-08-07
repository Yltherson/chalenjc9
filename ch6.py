chen ="ffhg dfygf hgjhj"
p = print

lc = chen.split(" ")

t = []
kar = ""

konk = ""
for el in lc:
    for i in el:
        t.append(i)
    t.reverse()
    kar = "".join(t)
p(kar)