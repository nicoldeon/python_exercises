import sys
import os.path
from abc import ABC, abstractmethod


class Number(ABC):
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

    @abstractmethod
    def find_factor(self):
        pass


class Factor(Number):
    def find_factor(self):
        return (lambda x: x > 1 and all(x % i != 0 for i in range(2, x)))


class PrimeFactor(Number):

    # find prime factor of that number
    def find_factor(self):
        prime_factors = []
        num = self.get_num()
        if num:
            # is_prime = (lambda x: x > 1 and all(
            #     x % i != 0 for i in range(2, x)))
            prime_factors = [factor for factor in range(
                2, num + 1) if num % factor == 0 and Factor.find_factor(factor)]
            return prime_factors
        else:
            return -1

    # print prime factor of that number
    def print_prime_factor(self):
        prime_factors = ""
        origin_num = self.get_num()
        num = self.get_num()
        ls_prime_factor = self.find_factor()

        if ls_prime_factor == -1:
            print("Dont have prime factor")
        else:
            for factor in ls_prime_factor:
                while num % factor == 0:
                    prime_factors = prime_factors + str(factor) + "x"
                    num = int(num / factor)
            prime_factors = prime_factors.rstrip("x")
            print(str(origin_num) + " = " + prime_factors)


def main():
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


if __name__ == '__main__':
    main()
