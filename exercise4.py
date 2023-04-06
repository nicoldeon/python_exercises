import sys
import os.path


class CalculationAngle:
    def __init__(self,
                 hour=None,
                 minute=None):
        self.hour = hour
        self.minute = minute

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        try:
            if hour != -1:
                hour = int(hour)
                if 0 <= hour <= 24:
                    self.hour = hour
                else:
                    print("Your hour is out of range!")
            else:
                print("You need to input some value!")
        except ValueError:
            print("You need to input a number!")

    def get_minute(self):
        return self.minute

    def set_minute(self, minute):
        try:
            if minute != -1:
                minute = int(minute)
                if 0 <= minute <= 60:
                    self.minute = minute
                else:
                    print("Your minute is out of range!")
            else:
                print("You need to input some value!")
        except ValueError:
            print("You need to input a number!")

    def read_from_file(self, url_path='exercise4.txt'):
        ls = []
        check_valid = True
        if os.path.exists(url_path):
            with open(url_path, 'r') as file:
                for line in file:
                    for num in line.split():
                        try:
                            num = int(num)
                            ls.append(int(num))
                        except ValueError:
                            print("Type input is not valid!")
                            check_valid = False
            if ls and check_valid:
                return ls
            else:
                return -1
        else:
            return -1

    # calculate angle between hour hand and minute hands
    def calculate_angle(self):

        hour = self.get_hour()
        minute = self.get_minute()

        if hour and minute:
            # reference to 12
            if hour == 12:
                hour = 0

            if minute == 60:
                minute = 0
                hour += 1

            if hour > 12:
                hour = hour - 12

            # calculate angle of hour hand, 1 hour -> hour hand move 30 degrees, 1 minute -> hour hand move 6/30 = 0.5 degrees
            angleHour = hour * 30 + minute * 0.5

            # calculate angle of minute hand, 1 minute -> minute hand move 6 degrees
            angleMinute = minute * 6

            # calculate angle between hour hand and minute hand
            ans = abs(angleHour - angleMinute)

            # return min between ans and 360 - ans
            return min(360 - ans, ans)
        else:
            return -1

    def print_angle(self):
        if self.calculate_angle() != -1:
            print("Angle between hour hand and minute hand is: ",
                  self.calculate_angle())
        else:
            print("Dont have value to calculate angle between two hands")


if __name__ == '__main__':
    cal_angle = CalculationAngle()
    n = len(sys.argv)
    if n > 1:
        ls = cal_angle.read_from_file(sys.argv[1])
    else:
        ls = cal_angle.read_from_file()

    if ls != -1:
        cal_angle.set_hour(ls[0])
        cal_angle.set_minute(ls[1])

    cal_angle.print_angle()
