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

    @classmethod
    def read_from_file(cls, url_path='exercise3.txt', *agrs, **kwargs):
        check_valid = True
        num = 0
        if agrs:
            url_path = agrs[0]
        if os.path.exists(url_path):
            with open(url_path, **kwargs) as file:
                for line in file:
                    for ele in line.split():
                        try:
                            num = int(ele)
                        except ValueError:
                            check_valid = False

            if num != 0 and check_valid:
                return cls(num)
            else:
                return -1
        else:
            return -1

    @abstractmethod
    def check_num(self):
        pass


class PrimeNumber(Number):
    def __init__(self, num=None):
        super().__init__(num)

    # check if number is prime number
    @staticmethod
    def check_num(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


class Factor(Number):
    def __init__(self, num=None):
        super().__init__(num)

    # check if number y is a factor of number x
    @staticmethod
    def check_num(num, factor):
        if num % factor == 0:
            return True
        return False


class PrimeFactor(Number):
    def __init__(self, num=None):
        super().__init__(num)

    def check_num(self):
        pass

    # find prime factor of number
    def find_prime_factor(self):
        prime_factors = []
        num = self.get_num()
        if num:
            factors = [factor for factor in range(
                2, num + 1) if Factor.check_num(num, factor)]
            prime_factors = list(
                filter(lambda x: PrimeNumber.check_num(x), factors))
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
    n = len(sys.argv)

    if n > 1:
        prime_factor = PrimeFactor.read_from_file(sys.argv[1], mode='r')
    else:
        prime_factor = PrimeFactor.read_from_file(mode='r')

    if prime_factor != -1:
        prime_factor.print_prime_factor()
    else:
        print("You have to input valid number!")


if __name__ == '__main__':
    main()
