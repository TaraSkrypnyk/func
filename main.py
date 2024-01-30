n = int(input('Vvedit chyslo: '))
        rez = False
        if n<0:
            n = int(input('Vvedit dodatne chyslo: '))
        if (n%2 != 0) and (n%3 != 0) and (n%5 != 0) and (n%7 != 0) and (n != 1) or (n == 2):
            rez = True
        print(rez)