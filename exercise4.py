class CalculationAngle:
    def __init__(self,
                 hour=None,
                 minute=None):
        self.hour = hour
        self.minute = minute

    def get_hour(self):
        return self.hour

    def set_hour(self):
        hour = int(input("Input hour: "))
        if hour != "":
            if type(hour) == int:
                if 0 <= hour <= 24:
                    self.hour = hour
                else:
                    print("Your hour is out of range!")
            else:
                print("Please input valid hour!")
        else:
            print("Can not let hour empty!")

    def get_minute(self):
        return self.minute

    def set_minute(self):
        minute = int(input("Input minute: "))
        if minute != "":
            if type(minute) == int:
                if 0 <= minute <= 60:
                    self.minute = minute
                else:
                    print("Your minute is out of range!")
            else:
                print("Please input valid minute!")
        else:
            print("Can not let hour empty!")

    # calculate angle between hour hand and minute hand
    def calculate_angle(self):
        hour = self.get_hour()
        minute = self.get_minute()

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


if __name__ == '__main__':
    cal_angle = CalculationAngle()
    cal_angle.set_hour()
    cal_angle.set_minute()
    angle = cal_angle.calculate_angle()
    print(angle)
