import sys
import os.path


class PrimeFactor:
    def __init__(self,
                 num=None):
        self.num = num

    def get_num(self):
        return self.num

    def set_num(self, num):
        try:
            if num == -1:
                print("You need to input some value!")
            else:
                num = int(num)
                if num > 0:
                    self.num = num
                else:
                    print("Please in put a positive number!")
        except ValueError:
            print("You need to input a number, please try again!")

    def read_from_file(self, url_path='exercise3.txt'):
        check_valid = True
        num = 0

        if os.path.exists(url_path):
            with open(url_path, 'r') as file:
                for line in file:
                    for ele in line.split():
                        try:
                            num = int(ele)
                        except ValueError:
                            check_valid = False
            if num != 0 and check_valid:
                return num
            else:
                return -1
        else:
            return -1

    # check if num input is prime number
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    # find prime factor of that number
    def find_prime_factor(self):
        prime_factors = []
        num = self.get_num()
        if num:
            for i in range(2, num):
                while num % i == 0 and self.is_prime(i):
                    num = int(num / i)
                    prime_factors.append(i)
                else:
                    if i > num:
                        break
            return prime_factors
        else:
            return -1

    # print prime factor of that number
    def print_prime_factor(self):
        prime_factors = ""
        num = self.get_num()

        if self.find_prime_factor() == -1:
            ls = []
        else:
            ls = self.find_prime_factor()

        if ls:
            n = len(ls)
            for i in range(n-1):
                prime_factors = prime_factors + str(ls[i]) + "x"
            prime_factors = prime_factors + str(ls[n-1])
            print(str(num) + " = " + prime_factors)
        else:
            print("Dont have prime factor")


if __name__ == '__main__':
    prime_factor = PrimeFactor()
    num = 0
    n = len(sys.argv)

    if n > 1:
        num = prime_factor.read_from_file(sys.argv[1])
    else:
        num = prime_factor.read_from_file()

    if num != -1:
        prime_factor.set_num(num)

    prime_factor.print_prime_factor()
