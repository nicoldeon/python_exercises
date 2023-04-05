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

    def calculate_angle(self):
        hour = self.get_hour()
        minute = self.get_minute()
        angle_bw_hour_minute = 0


if __name__ == '__main__':
    cal_angle = CalculationAngle()
    cal_angle.set_hour()
    cal_angle.set_minute()
    print(cal_angle.get_hour())
    print(cal_angle.get_minute())
