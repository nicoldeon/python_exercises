class PrimeFactor:
    def __init__(self,
                 num=None):
        self.num = num

    def get_num(self):
        return self.num

    def set_num(self):
        while True:
            try:
                num = input("Input a number: ")
                if num:
                    num = int(num)
                    if num > 0:
                        self.num = num
                        break
                    else:
                        print("Please in put a positive number!")
                        print()
                else:
                    print("You need to input some value!")
                    print()
            except ValueError:
                print("You need to input a number, please try again!")
                print()

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
        for i in range(2, num):
            while num % i == 0 and self.is_prime(i):
                num = int(num / i)
                prime_factors.append(i)
            else:
                if i > num:
                    break
        return prime_factors

    # print prime factor of that number
    def print_prime_factor(self):
        prime_factors = ""
        num = self.get_num()
        ls = self.find_prime_factor()
        n = len(ls)
        for i in range(n-1):
            prime_factors = prime_factors + str(ls[i]) + "x"
        prime_factors = prime_factors + str(ls[n-1])
        print(str(num) + " = " + prime_factors)


if __name__ == '__main__':
    prime_factor = PrimeFactor()
    prime_factor.set_num()
    prime_factor.print_prime_factor()
