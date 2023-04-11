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
        if 0 <= minute <= 60:
            self.minute = minute
        else:
            print("Your minute is out of range!")

    # calculate angle of minute hand, 1 minute -> minute hand move 6 degrees
    def get_angle(self):
        return self.get_minute() * 6


class HourAngle(MinuteAngle):
    def __init__(self, hour=None, minute=None):
        super().__init__(minute)
        self.hour = hour

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        if 0 <= hour <= 24:
            self.hour = hour
        else:
            print("Your hour is out of range!")

    def convert_time(self):
        if self.hour == 24:
            self.hour = 0
        if self.hour > 12:
            self.hour = self.hour - 12
        if self.minute == 60:
            super().set_minute = 0
            self.set_hour += 1

    # calculate angle of hour hand, 1 hour -> hour hand move 30 degrees
    # 1 minute -> hour hand move 30/60 = 0.5 degrees
    def get_angle(self):
        return self.get_hour() * 30 + super().get_minute() * 0.5

    def get_minute_angle(self):
        return super().get_angle()


class Clock:
    def __init__(self,
                 hour=None,
                 minute=None):
        self.angles = HourAngle(hour, minute)

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

    def calc_angle(self):
        self.angles.convert_time()
        calc_hour_ans = self.angles.get_angle()
        calc_mins_ans = self.angles.get_minute_angle()
        ans = abs(calc_hour_ans - calc_mins_ans)
        return min(360 - ans, ans)


def main():

    clock = Clock()
    n = len(sys.argv)

    if n > 1:
        ls = clock.read_from_file(sys.argv[1])
    else:
        ls = clock.read_from_file()

    if ls != -1:
        calc_ans = Clock(ls[0], ls[1])
        ans = calc_ans.calc_angle()
        if ans:
            print("Angle between hour and minute hand is: ", ans)
        else:
            print("Don't have angle between hour hand minute hand!")
    else:
        print("You have to input valid value")


if __name__ == '__main__':
    main()
