def get_sum_of_list(list,  rez = 0):
    for i in range(len(list)):
        rez += list[i]
    return rez


if __name__ == "__main__":
    try:
        list = [1, 12, 6, 3, 19, 8, 4, 5]
        print('sum = ', get_sum_of_list(list))
    except Exception as e:
        print(e)