def get_count_from_list(list, i=0, par=0, nepar=0, dod=0, vid=0):
    if i < len(list):
        if list[i] >= 0:
            dod +=1
        else:
            vid +=1
        if list[i]%2 == 0 and list[i]>=0:
            par +=1
        elif list[i]%2 == 1 and list[i]>=0:
            nepar +=1
        return get_count_from_list(list, i + 1, par, nepar, dod, vid)
    return 'parnyh=',  par, 'neparnyh=',nepar, 'dodatnih=', dod, 'vidyemnyh=',vid


if __name__ == "__main__":
    try:
        list = [1, 42, 6, 3, -19, -8, 4, 5]
        print(list)
        print(get_count_from_list(list))
    except Exception as e:
        print(e)
