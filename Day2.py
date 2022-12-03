Score = 0
Score2 = 0
with open('Day2.txt', 'r') as file:
    for x in file:
        f1=x[0]
        f2=x[2]
        if f1 == 'A':
            if f2 == 'Y':
                Score += 8
            elif f2 == 'X':
                Score += 4
            elif f2 == 'Z':
                Score += 3
        elif f1 == 'B':
            if f2 == 'Y':
                Score += 5
            elif f2 == 'X':
                Score += 1
            elif f2 == 'Z':
                Score += 9
        elif f1 == 'C':
            if f2 == 'Y':
                Score += 2
            elif f2 == 'X':
                Score += 7
            elif f2 == 'Z':
                Score += 6

        if f1 == 'A':
            if f2 == 'Y':
                Score2 += 4
            elif f2 == 'X':
                Score2 += 3
            elif f2 == 'Z':
                Score2 += 8
        elif f1 == 'B':
            if f2 == 'Y':
                Score2 += 5
            elif f2 == 'X':
                Score2 += 1
            elif f2 == 'Z':
                Score2 += 9
        elif f1 == 'C':
            if f2 == 'Y':
                Score2 += 6
            elif f2 == 'X':
                Score2 += 2
            elif f2 == 'Z':
                Score2 += 7
    print("First Part:", Score)
    print("Second Part:", Score2)
