count = 0
count2 = 0
with open('Day4.txt', 'r') as file:
    for x in file:

        x = x.rstrip().split(",")
        Elf1 = x[0]
        Elf2 = x[1]
        Elf1 = Elf1.split("-")
        Elf2 = Elf2.split("-")
        Elf1[0] = int(Elf1[0])
        Elf1[1] = int(Elf1[1])
        Elf2[0] = int(Elf2[0])
        Elf2[1] = int(Elf2[1])
        print(Elf1,Elf2)
        n = 0
        if Elf1[0] >= Elf2[0] and Elf1[1] <= Elf2[1]:
            count += 1
            count2 += 1
        elif Elf1[0] <= Elf2[0] and Elf1[1] >= Elf2[1]:
            count += 1
            count2 += 1
        else:
            for q in range(Elf1[0],Elf1[1]):
                if q in range(Elf2[0],Elf2[1]+1):
                    count2 += 1
                    n = 1
                    break
        
            for o in range(Elf2[0],Elf2[1]):
                if o in range(Elf1[0],Elf1[1]+1) and n==0:
                    count2 += 1
                    break


    print("Part1:",count)
    print("Part2:",count2)

