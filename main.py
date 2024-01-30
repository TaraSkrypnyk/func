def proste_chislo(list):
    rez = 0
    for i in range(len(list)):
        if (list[i] % 2 != 0) and (list[i] % 3 != 0) and (list[i] % 5 != 0) and (list[i] % 7 != 0) and (list[i] != 1) or (list[i] == 2 or (list[i] == 3) or (list[i] == 5) or (list[i] == 5)):
            rez += 1
            print(list[i])
    return rez


if __name__ == "__main__":
    try:
        list = [1, 12, 6, 3, 19, 8, 4, 5]
    except Exception as e:
        print(e)