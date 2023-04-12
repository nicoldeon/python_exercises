import sys
import os.path
from abc import ABC, abstractmethod


class ClockAngle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_angle(self):
        raise NotImplementedError("Subclass must be implemented this method")


class MinuteAngle(ClockAngle):
    def __init__(self, minute=None):
        self.minute = minute

    def get_minute(self):
        return self.minute

    def set_minute(self, minute):
        if 0 <= minute <= 60:
            self.minute = minute
        else:
            self.minute = -1

    # calculate angle of minute hand, 1 minute -> minute hand move 6 degrees
    def get_angle(self):
        return self.get_minute() * 6


class HourAngle(ClockAngle):
    def __init__(self,
                 hour=None,
                 minuteAngle=MinuteAngle()):
        self.hour = hour
        self.minute_ans = minuteAngle

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        if 0 <= hour <= 24:
            self.hour = hour
        else:
            self.hour = -1

    def get_minute_ans(self):
        return self.minute_ans

    def set_minute_ans(self, minuteAngle):
        self.minute_ans = minuteAngle

    # calculate angle of hour hand, 1 hour -> hour hand move 60 degrees
    # one minute -> hour hand move 30/60 = 0.5 degrees
    def get_angle(self):
        return (self.get_hour()*30 + self.get_minute_ans().get_minute()*0.5)*-1


class Clock:
    def __init__(self, ls_hands=[]):
        self.ls_hands = ls_hands

    def get_ls_ans_hands(self):
        return self.ls_hands

    def set_ls_ans_hands(self, ls_hands):
        self.ls_hands = ls_hands

    # convert time reference to 12
    @staticmethod
    def convert_time(hour, minute):
        if 0 <= hour <= 24 and 0 <= minute <= 60:
            if hour == 12 or hour == 24:
                hour = 0
            if hour > 12:
                hour -= 12
            if minute == 60:
                minute = 0
                hour += 1
        else:
            hour = -1
            minute = -1
        return hour, minute

    # read value of hour and minute from file
    @classmethod
    def read_from_file(cls, url_path='exercise4.txt', *agrs, **kwargs):
        valid = True
        ls = []
        if agrs:
            url_path = agrs[0]
        if os.path.exists(url_path):
            with open(url_path, **kwargs) as file:
                try:
                    ls = [int(num) for line in file for num in line.split(":")]
                except ValueError:
                    valid = False
            check_valid = (lambda x, y: x if x and valid else -1)
            if check_valid(ls, valid) != -1:
                hour, minute = Clock.convert_time(ls[0], ls[1])
                if hour != -1 and minute != -1:
                    hour_ans = HourAngle(hour, MinuteAngle(minute))
                    mins_ans = MinuteAngle(minute)
                    ls_angle = [hour_ans, mins_ans]
                    return cls(ls_angle)
                else:
                    return -1
            else:
                return -1
        else:
            return -1

    # calculate angle between hour hand and minute hand
    def calc_angle(self):
        ans = abs(sum([hand.get_angle() for hand in self.ls_hands]))
        return ans


def main():
    n = len(sys.argv)
    if n > 1:
        clock = Clock.read_from_file(sys.argv[1], mode='r')
    else:
        clock = Clock.read_from_file(mode='r')

    if clock != -1:
        ans = clock.calc_angle()
        if ans != -1:
            print("Angle between hour hand and minute hand is: ", ans)
        else:
            print("You must input valid range of hour and minute!")
    else:
        print("Don't have value to calculate angle between two hand of clock")


if __name__ == '__main__':
    main()
