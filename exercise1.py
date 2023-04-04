def find_max_in_list(lis):
    # read list from file
    with open('exercise1.txt', 'r') as file:
        for line in file:
            for num in line.split():
                ls.append(int(num))

    max_ls = 0

    # find max in list
    for x in lis:
        if x > max_ls:
            max_ls = x
    return max_ls


if __name__ == "__main__":
    ls = []
    print(find_max_in_list(ls))
