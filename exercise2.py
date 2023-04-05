from exercise1 import find_max_in_list
import sys
import os.path


# input file name from command line
def user_input_file():
    n = len(sys.argv)
    file_name = ""
    if n > 1:
        file_name = sys.argv[1]
    else:
        file_name = "exercise2.txt"
    return file_name


# read list of number from file user input
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


# find second max element in list
def find_second_max_list(ls):
    # if length of list is 0, dont exist second max element
    if (len(ls) == 0):
        return -1

    # if length of list is 1, dont exist second max element
    if (len(ls) == 1):
        return -1

    # find max in list
    max_ls = find_max_in_list(ls)
    second_max = 0

    # loop to assign element to second_max with condition that element is not equal to max_ls
    for x in ls[:]:
        if x != max_ls:
            second_max = x
            break

    # get index of second_max
    index_scm = ls.index(second_max)

    # find second max in list loop from index_scm + 1
    for x in ls[index_scm+1:]:
        if x > second_max and x < max_ls:
            second_max = x

    return second_max


if __name__ == "__main__":
    ls = read_from_file()
    print(find_second_max_list(ls))
