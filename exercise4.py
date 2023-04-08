import sys
import os.path
from abc import ABC, abstractmethod


class Clock(ABC):
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
                            check_valid = False

            if ls and check_valid:
                return ls
            else:
                return -1
        else:
            return -1

    @abstractmethod
    def calc_angle(self):
        pass


class CalculateHourAngle(Clock):
    def calc_angle(self):
        hour = self.get_hour()
        minute = self.get_minute()
        if hour and minute:
            if hour == 24:
                hour = 0
            if hour > 12:
                hour = hour - 12
            if minute == 60:
                minute = 0
                hour += 1

            # calculate angle of hour hand, 1 hour -> hour hand move 30 degrees, 1 minute -> hour hand move 6/30 = 0.5 degrees
            get_hour_ans = (lambda x, y: x*30 + y*0.5)
            return get_hour_ans(hour, minute)
        else:
            return -1


class CalculateMinuteAngle(Clock):
    def calc_angle(self):
        hour = self.get_hour()
        minute = self.get_minute()
        if hour and minute:
            if hour == 24:
                hour = 0
            if hour > 12:
                hour = hour - 12
            if minute == 60:
                minute = 0
                hour += 1
            # calculate angle of minute hand, 1 minute -> minute hand move 6 degrees
            get_minute_ans = (lambda x: x*6)
            return get_minute_ans(minute)
        else:
            return -1


class CalculateAngle(Clock):
    # calculate angle between hour hand and minute hands
    def calc_angle(self):

        hour = self.get_hour()
        minute = self.get_minute()
        hour_ans = CalculateHourAngle(hour, minute)
        min_ans = CalculateMinuteAngle(hour, minute)

        if hour and minute:
            # calculate angle between hour hand and minute hand
            if hour_ans.calc_angle() != -1 and min_ans.calc_angle != -1:
                ans = abs(hour_ans.calc_angle() -
                          min_ans.calc_angle())
                # return min between ans and 360 - ans
                return min(360 - ans, ans)
            else:
                return -1
        else:
            return -1

    def print_angle(self):
        ans = self.calc_angle()
        if ans != -1:
            print("Angle between hour hand and minute hand is: ",
                  self.calc_angle())
        else:
            print("Dont have value to calculate angle between two hands")


def main():
    cal_angle = CalculateAngle()
    n = len(sys.argv)
    if n > 1:
        ls = cal_angle.read_from_file(sys.argv[1])
    else:
        ls = cal_angle.read_from_file()

    if ls != -1:
        cal_angle.set_hour(ls[0])
        cal_angle.set_minute(ls[1])

    cal_angle.print_angle()


if __name__ == '__main__':
    main()
