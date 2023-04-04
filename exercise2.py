def find_second_max_list(lis):
    # read list from file
    with open('exercise2.txt', 'r') as file:
        for line in file:
            for num in line.split():
                ls.append(int(num))

    n = len(ls)
    # sort list descending
    for i in range(n):
        for j in range(0, n - i - 1):
            if ls[j] < ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]

    # return the second element (second max) of list descending
    return ls[1]


if __name__ == "__main__":
    ls = []
    print(find_second_max_list(ls))
