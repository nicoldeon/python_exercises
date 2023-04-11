import sys
import os.path
from abc import ABC, abstractmethod


class ClockAngle(ABC):

    @abstractmethod
    def get_angle(self):
        pass


class MinuteAngle(ClockAngle):
    def __init__(self, minute=None):
        self.minute = minute

    def get_minute(self):
        return self.minute

    def set_minute(self, minute):
        self.minute = minute

    def get_angle(self):
        return self.minute*6


class HourAngle(ClockAngle):
    def __init__(self,
                 hour=None,
                 MinuteAngle=None):
        self.hour = hour
        self.minute_ans = MinuteAngle

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        self.hour = hour

    def get_minute_ans(self):
        return self.minute_ans

    def set_minute_ans(self, MinuteAngle):
        self.minute_ans = MinuteAngle

    def get_angle(self):
        return self.hour*30 + self.get_minute_ans().get_minute()*0.5


class Clock:
    def read_from_file(self, url_path='exercise4.txt'):
        valid = True
        ls = []
        if os.path.exists(url_path):
            with open(url_path, 'r') as file:
                try:
                    ls = [int(num) for line in file for num in line.split(":")]
                except ValueError:
                    valid = False
            check_valid = (lambda x, y: x if x and valid else -1)
            if check_valid(ls, valid) != -1:
                return ls
            else:
                return -1
        else:
            return -1

    # calculate angle between hour hand and minute hand
    def calc_angle(self, hour, minute):
        if 0 <= hour <= 24 and 0 <= minute <= 60:
            if hour == 12:
                hour = 0
            if hour > 12:
                hour -= 12
            if minute == 60:
                minute = 0
                hour += 1
        else:
            hour = -1
            minute = -1
        hour_ans = HourAngle(hour, MinuteAngle(minute))
        if hour_ans.get_hour() != -1 and hour_ans.get_minute_ans().get_minute() != -1:
            calc_hour_ans = hour_ans.get_angle()
            calc_mins_ans = hour_ans.get_minute_ans().get_angle()
            ans = abs(calc_hour_ans - calc_mins_ans)
            return min(360 - ans, ans)
        else:
            -1


def main():

    clock = Clock()
    n = len(sys.argv)

    if n > 1:
        ls = clock.read_from_file(sys.argv[1])
    else:
        ls = clock.read_from_file()

    if ls != -1:
        ans = clock.calc_angle(ls[0], ls[1])
        if ans:
            print("Angle between hour and minute hand is: ", ans)
        else:
            print("Don't have angle between hour hand minute hand!")
    else:
        print("You have to input valid value")


if __name__ == '__main__':
    main()
