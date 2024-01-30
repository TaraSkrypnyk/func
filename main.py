def delete_from_list(list1, list2):
    res_list = list1 + list2
    return res_list



if __name__ == "__main__":
    try:
        list1 = [1, 12, 6, 3, 19, 8, 4, 5]
        list2 = [0, -5, 15]
        print(delete_from_list(list1, list2))
    except Exception as e:
        print(e)