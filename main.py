def get_mirror_list(list, i=0, rez_list=[]):
    if i < len(list):
        rez_list.append(list[(i+1) * (-1)])
        return get_mirror_list(list, i + 1, rez_list)
    return rez_list


if __name__ == "__main__":
    try:
        list = [1, 42, 6, 3, -19, -8, 4, 5]
        print(get_mirror_list(list))
    except Exception as e:
        print(e)
