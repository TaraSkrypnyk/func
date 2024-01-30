def get_product_of_list(list):
    rez = list[0]
    for i in range(len(list)):
        if rez > list[i]:
            rez = list[i]
    return rez


if __name__ == "__main__":
    try:
        list = [1, 12, 6, 3, 19, 8, 4, 5]
        print('lower in list = ', get_product_of_list(list))
    except Exception as e:
        print(e)
