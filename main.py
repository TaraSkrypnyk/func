def find_in_list(list, i=0, rez = False):
    if i < len(list):
        x = int(input('Vvedit chyslo dlya poshuku: '))
        if x in list:
            rez = True
            return rez
        else:
            return rez
        return find_in_list(list, i + 1, rez)
    return rez


if __name__ == "__main__":
    try:
        list = [1, 42, 6, 3, -19, -8, 4, 5]
        print(list)
        print(find_in_list(list))
    except Exception as e:
        print(e)