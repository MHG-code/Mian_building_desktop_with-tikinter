def check_name_in_dic_or_not(name, dic):
    for i in range(len(dic)):
        if name in dic[i]:
            return True
    return False