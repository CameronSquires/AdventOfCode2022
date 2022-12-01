maxList = []
with open('Q1.txt', 'r') as file:
    p = file.read()
    ElfCals = [[line.split(" ")[0] for line in calCounts.split("\n")] for calCounts in p.split("\n\n")]
    for x in range(0, len(ElfCals)):        
        total = sum(int(cal) for cal in ElfCals[x])
        maxList.append(total)
    
    maxForList = max(maxList)
    maxList.remove(maxForList)
    secondMax = max(maxList)
    maxList.remove(secondMax)
    lastMax = max(maxList)
    top3count = 0 + maxForList
    top3count += secondMax
    top3count += lastMax #I know this is not efficient, but I was trying to do this as fast as possible.
    print("top:", maxForList)
    print("top 3:", top3count)
