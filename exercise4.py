class CalculationAngle:
    def __init__(self,
                 hour=None,
                 minute=None):
        self.hour = hour
        self.minute = minute

    def get_hour(self):
        return self.hour

    def set_hour(self):
        try:
            hour = input("Input hour: ")
            if hour:
                hour = int(hour)
                if 0 <= hour <= 60:
                    self.hour = hour
                else:
                    print("Your minute if out of range!")
            else:
                print("You need to input some value!")
        except ValueError:
            print("You need to input a number!")

    def get_minute(self):
        return self.minute

    def set_minute(self):
        try:
            minute = input("Input minute: ")
            if minute:
                minute = int(minute)
                if 0 <= minute <= 60:
                    self.minute = minute
                else:
                    print("Your minute if out of range!")
            else:
                print("You need to input some value!")
        except ValueError:
            print("You need to input a number!")

    # calculate angle between hour hand and minute hands
    def check_if_int(self, num):
        if type(num) == int:
            return True
        return False

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
            print("Please input a hour value and a minute value!")


if __name__ == '__main__':
    cal_angle = CalculationAngle()
    cal_angle.set_hour()
    cal_angle.set_minute()
    angle = cal_angle.calculate_angle()
    print(angle)
