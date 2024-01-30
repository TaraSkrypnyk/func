def get_factorial_list(list, i=0, rez_list=[]):
    if i < len(list):
        factorial = 1
        while list[i] > 1:
            factorial *= list[i]
            list[i] -= 1
        rez_list.append(factorial)
        return get_factorial_list(list, i + 1, rez_list)
    return rez_list


if __name__ == "__main__":
    try:
        list = [1, 12, 6, 3, 19, 8, 4, 5]
        print(get_factorial_list(list))
    except Exception as e:
        print(e)