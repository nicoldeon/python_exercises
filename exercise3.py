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
        if num > 0:
            self.num = num
        else:
            print("Please input a positive number!")

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
    def check_num(self):
        pass


class PrimeNumber(Number):
    # check if number is prime number
    def check_num(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


class Factor(Number):
    # check if number y is a factor of number x
    def check_num(self, factor):
        if self.num % factor == 0:
            return True
        return False


class PrimeFactor(Number):
    def check_num(self):
        pass

        # find prime factor of number
    def find_prime_factor(self):
        prime_factors = []
        num = self.get_num()
        check_is_prime = PrimeNumber(self.num)
        check_factor = Factor(self.num)
        if num:
            factors = [factor for factor in range(
                2, num + 1) if check_factor.check_num(factor)]
            prime_factors = list(
                filter(lambda x: check_is_prime.check_num(x), factors))
            return prime_factors
        else:
            return -1

    # print out prime factos of number
    def print_prime_factor(self):
        prime_factors = ""
        origin_num = self.get_num()
        num = self.get_num()
        ls_prime_factors = self.find_prime_factor()
        if ls_prime_factors == -1:
            print("Dont have prime factor")
        else:
            for factor in ls_prime_factors:
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
    else:
        print("You have to input valid number!")

    prime_factor.print_prime_factor()


if __name__ == '__main__':
    main()
