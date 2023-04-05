class PrimeFactor:
    def __init__(self,
                 num=None):
        self.__num = num

    def get_num(self):
        return self.__num

    def set_num(self):
        num = int(input("Input your number you want to find prime factor:"))
        if type(num) == int:
            if num > 0:
                self.__num = num
                print("Congrats, the value has been set to: ", self.__num)
            else:
                print("Please input a positive number")
        else:
            print("Please input a valid number!")

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


A = PrimeFactor()
A.set_num()
A.print_prime_factor()
