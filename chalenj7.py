chenn = "abcdef ghijklmnop dal"

voy = ["a","e","i","o","u","y"]

for i in range(1,len(chenn)):
    if(chenn[i] in voy):
        chenn = chenn.replace(chenn[i-1], "*",1)

print(chenn)