import sys
import os.path


def user_input_file():
    n = len(sys.argv)
    file_name = ""
    if n > 1:
        file_name = sys.argv[1]
    else:
        file_name = "exercise1.txt"
    return file_name


def read_from_file():
    ls = []
    file_name = user_input_file()
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                for num in line.split():
                    ls.append(int(num))
    else:
        print("No such file!")
    return ls


def find_max_in_list(ls):
    # if length of list is 0, return -1, dont exits max value
    if (len(ls) == 0):
        return -1

    # if length of list is 1, max element is the only element of the list
    if len(ls) == 1:
        return ls[0]

    # assgin max is the first element
    max_ls = ls[0]

    # find max in list from the second element
    for x in ls[1:]:
        if x > max_ls:
            max_ls = x

    return max_ls


if __name__ == "__main__":
    ls = read_from_file()
    print(find_max_in_list(ls))
