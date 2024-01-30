def delete_from_list(list, d):
    rez = 0
    i = 0
    l=len(list)
    while i <= l:
        if list[i] == d:
            list.pop(i)
            l -= 1
            rez += 1
        i += 1
    return rez, list


if __name__ == "__main__":
    try:
        list = [1, 12, 6, 3, 19, 8, 4, 5]
        print(list)
        d = int(input('Введіть число яке хочете видалити зі списку: '))
        print(delete_from_list(list, d))
    except Exception as e:
        print(e)