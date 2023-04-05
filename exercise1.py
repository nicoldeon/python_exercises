import sys
import os.path


# read list of number from file user input
def read_from_file(url_file_path):
    ls = []
    if os.path.exists(url_file_path):
        with open(url_file_path, 'r') as file:
            for line in file:
                for num in line.split():
                    ls.append(int(num))
    else:
        print("No such file!")
    return ls


# find max in list
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
    # input file path from command line
    n = len(sys.argv)
    url_file_path = ""
    if n > 1:
        url_file_path = sys.argv[1]
    else:
        url_file_path = "exercise1.txt"

    ls = read_from_file(url_file_path)
    print(find_max_in_list(ls))
