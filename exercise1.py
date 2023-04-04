import random


def input_list(lis):
    n = int(input("Input number of elements of list:"))
    if type(n) == int:
        for i in range(n):
            if type(i) == int:
                ele = int(input(f"Input element {i+1}: "))
                lis.append(ele)
            else:
                print("The input type is not integer, please try again")
    else:
        print("The input type is not integer, please try again")
    return lis


def find_max_in_list(lis):
    max_ls = 0
    for x in lis:
        if type(x) == int:
            if x > max_ls:
                max_ls = x
        else:
            continue
    return max_ls


if __name__ == "__main__":
    ls = []
    input_list(ls)
    print(find_max_in_list(ls))
