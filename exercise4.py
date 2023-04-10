import sys
import os.path
from abc import ABC, abstractmethod


class ClockAngle(ABC):

    @abstractmethod
    def get_angle(self):
        pass


class HourAngle(ClockAngle):
    # calculate angle of hour hand, 1 hour -> hour hand move 30 degrees
    # 1 minute -> hour hand move 30/60 = 0.5 degrees
    def get_angle(self, hour, minute):
        return hour * 30 + minute * 0.5


class MinuteAngle(ClockAngle):
    # calculate angle of minute hand, 1 minute -> minute hand move 6 degrees
    def get_angle(self, minute):
        return minute * 6


class Clock(ClockAngle):
    def __init__(self,
                 hour=None,
                 minute=None,
                 second=None):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        if 0 <= hour <= 24:
            self.hour = hour
        else:
            print("Your hour is out of range!")

    def get_minute(self):
        return self.minute

    def set_minute(self, minute):
        if 0 <= minute <= 60:
            self.minute = minute
        else:
            print("Your minute is out of range!")

    def get_second(self):
        return self.second

    def set_second(self, second):
        self.second = second

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

    def convert_time(self, hour, minute):
        if hour == 24:
            hour = 0
        if hour > 12:
            hour = hour - 12
        if minute == 60:
            minute = 0
            hour += 1
        return hour, minute

    def get_angle(self):
        self.hour, self.minute = self.convert_time(self.hour, self.minute)
        hour_ans = HourAngle()
        mins_ans = MinuteAngle()
        ans = abs(hour_ans.get_angle(
            self.hour, self.minute) - mins_ans.get_angle(self.minute))
        return min(360 - ans, ans)


def main():

    clock = Clock()
    n = len(sys.argv)

    if n > 1:
        ls = clock.read_from_file(sys.argv[1])
    else:
        ls = clock.read_from_file()

    if ls != -1:
        clock.set_hour(ls[0])
        clock.set_minute(ls[1])
        ans = clock.get_angle()
        if ans:
            print("Angle between hour and minute hand is: ", ans)
        else:
            print("Don't have angle between hour hand minute hand!")
    else:
        print("You have to input valid value")


if __name__ == '__main__':
    main()
