def read_from_file(ls):
    with open('exercise2.txt', 'r') as file:
        for line in file:
            for num in line.split():
                ls.append(int(num))
    return ls


def find_max_in_list(ls):
    # if length of list is 0, dont exist max value
    if (len(ls) == 0):
        return -1

    # if length of list is 1, max element is the only element of the list
    if len(ls) == 1:
        return ls[0]

    max_ls = ls[0]

    # find max in list
    for x in ls[1:]:
        if x > max_ls:
            max_ls = x

    return max_ls


def find_second_max_list(ls):
    # if length of list is 0, dont exist second max element
    if (len(ls) == 0):
        return -1

    # if length of list is 1, dont exist second max element
    if (len(ls) == 1):
        return -1

    # find max in list
    max_ls = find_max_in_list(ls)

    if (ls[0] == max_ls):
        second_max = ls[1]
    else:
        second_max = ls[0]

    # find second max in list
    if (second_max == ls[1]):
        for x in ls[2:]:
            if x > second_max and x < max_ls:
                second_max = x
    else:
        for x in ls[1:]:
            if x > second_max and x < max_ls:
                second_max = x

    return second_max


if __name__ == "__main__":
    ls = []
    read_from_file(ls)
    print(find_second_max_list(ls))
