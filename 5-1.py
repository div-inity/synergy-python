s = input()
count = 0
for i in range(len(s)) :
    a = i * (-1) -1
    if (s[i] == s[a]) :
        count += 1

if count == len(s) :
    print("yes")
else :
    print("no")
