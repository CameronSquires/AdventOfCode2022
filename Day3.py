alphabet = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum1 = 0
sum2 = 0
p = 0
with open('Day3.txt', 'r') as file:
    for g in file:
        g = g.rstrip()
        f=len(g)/2
        f = int(f)
        comp1 = g[0:f]
        comp2 = g[f::]
        for x in comp1:
            for y in comp2:
                if x==y:
                    sum1 += alphabet.index(x)
                    break
                    
                
            if x == y:
                break
    print("sum1:", sum1)
with open('Day3.txt', 'r') as file:
    line1 = 0
    line2 = 0
    line3 = 0
    while True and line1 or line2 or line3 != "":
        line1 = file.readline()
        line1 = line1.rstrip()
        line2 = file.readline()
        line2 = line2.rstrip()
        line3 = file.readline()
        line3 = line3.rstrip()
        for x in line1:
            for y in line2:
                for z in line3:
                    if x == y == z:
                        if x.islower():
                            sum2 += alphabet.index(x)
                            break
                if x == y == z and x.islower():
                    break
            if x == y == z and x.islower():
                break
        for x in line1:
            for y in line2:
                for z in line3:
                    if x == y == z:
                        if x.isupper():
                            sum2 += alphabet.index(x)
                            break
                if x == y == z and x.isupper():
                    break
            if x == y == z and x.isupper():
                break
print("sum2:",sum2)
