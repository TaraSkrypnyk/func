def get_max_in_list(list):
    rez = list[0]
    for i in range(len(list)):
        if rez < list[i]:
            rez = list[i]
    return rez


if __name__ == "__main__":
    try:
        list = [1, 12, 6, 3, 19, 8, 4, 5]
        print('max in list = ', get_max_in_list(list))
    except Exception as e:
        print(e)
