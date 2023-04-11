import sys
import os.path
from abc import ABC, abstractmethod


class ClockAngle(ABC):
    def __init__(self):
        pass

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
        return self.get_hour()*30 + self.get_minute_ans().get_minute()*0.5


class Clock:
    def __init__(self, hourAngle=HourAngle()):
        self.hour_ans = hourAngle

    def get_hour_ans(self):
        return self.hour_ans

    def set_hour_ans(self, hourAngle):
        self.hour_ans = hourAngle

    # convert time reference to 12
    @staticmethod
    def convert_time(hour, minute):
        if hour == 12:
            hour = 0
        if hour > 12:
            hour -= 12
        if minute == 60:
            minute = 0
            hour += 1
        return hour, minute

    # read value of hour and minute from file
    @classmethod
    def read_from_file(cls, *agrs, **kwargs):
        valid = True
        ls = []
        if agrs:
            url_path = agrs[0]
        else:
            url_path = 'exercise4.txt'
        if os.path.exists(url_path):
            with open(url_path, **kwargs) as file:
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
        hour = self.hour_ans.get_hour()
        minute = self.hour_ans.get_minute_ans().get_minute()
        hour, minute = Clock.convert_time(hour, minute)
        hour_ans2 = HourAngle()
        hour_ans2.set_hour(hour)
        hour_ans2.get_minute_ans().set_minute(minute)

        if hour_ans2.get_hour() != -1 and hour_ans2.get_minute_ans().get_minute() != -1:
            calc_hour_ans = self.hour_ans.get_angle()
            calc_mins_ans = self.hour_ans.get_minute_ans().get_angle()
            result = abs(calc_hour_ans - calc_mins_ans)
            return min(360 - result, result)
        else:
            return -1


def main():
    n = len(sys.argv)
    if n > 1:
        ls = Clock.read_from_file(sys.argv[1], mode='r')
    else:
        ls = Clock.read_from_file(mode='r')

    if ls != -1:
        minute_ans = MinuteAngle(ls[1])
        hour_ans = HourAngle(ls[0], minute_ans)
        clock = Clock(hour_ans)
        ans = clock.calc_angle()
        if ans != -1:
            print("Angle between hour hand and minute hand is: ", ans)
        else:
            print("Don't have value of angle between hour hand and minute hand")
    else:
        print("Don't have value to calculate angle between two hand of clock")


if __name__ == '__main__':
    main()
