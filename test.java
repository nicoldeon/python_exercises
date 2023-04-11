import java.io.File
import java.io.IOException
import java.nio.charset.StandardCharsets
import java.nio.file.Files
import java.util.List

public abstract class ClockAngle {
    public abstract float getAngle()
}

    class MinuteAngle extends ClockAngle {
    private int minute

    public MinuteAngle(int minute) {
        this.minute = minute
    }

    public int getMinute() {
        return minute
    }

    public void setMinute(int minute) {
        if (0 <= minute & & minute <= 60) {
            this.minute = minute
        } else {
            this.minute = -1
        }
    }

    @ Override
    public float getAngle() {
        return minute * 6
    }
    }

    class HourAngle extends ClockAngle {
    private int hour
    private MinuteAngle minuteAngle

    public HourAngle(int hour, MinuteAngle minuteAngle) {
        this.hour = hour
        this.minuteAngle = minuteAngle
    }

    public int getHour() {
        return hour
    }

    public void setHour(int hour) {
        if (0 <= hour & & hour <= 24) {
            this.hour = hour
        } else {
            this.hour = -1
        }
    }

    public MinuteAngle getMinuteAngle() {
        return minuteAngle
    }

    public void setMinuteAngle(MinuteAngle minuteAngle) {
        this.minuteAngle = minuteAngle
    }

    @ Override
    public float getAngle() {
        return hour * 30 + minuteAngle.getAngle() * 0.5f
    }
    }

    class Clock {
    private HourAngle hourAngle

    public Clock(HourAngle hourAngle) {
        this.hourAngle = hourAngle
    }

    public HourAngle getHourAngle() {
        return hourAngle
    }

    public void setHourAngle(HourAngle hourAngle) {
        this.hourAngle = hourAngle
    }

    public static int[] readFromFile(String url) {
        boolean valid = true
        int[] ls = new int[0]
        File file = new File(url)
        if (file.exists()) {
            try {
                List < String > lines = Files.readAllLines(file.toPath(), StandardCharsets.UTF_8)
                String[] parts = lines.get(0).split(":")
                ls = new int[parts.length]
                for (int i=0
                     i < parts.length
                     i++) {
                    ls[i] = Integer.parseInt(parts[i])
                }
            } catch(NumberFormatException | IOException e) {
                valid = false
            }

            if (ls.length > 0 & & valid) {
                return ls
            } else {
                return new int[]{-1}
            }
        } else {
            return new int[]{-1}
        }
    }

    public float calcAngle() {
        int hour = hourAngle.getHour()
        int minute = hourAngle.getMinuteAngle().getMinute()
        if (hour == 12) {
            hour = 0
        }
        if (hour > 12) {
            hour -= 12
        }
        if (minute == 60) {
            minute = 0
            hour += 1
        }

        HourAngle hourAns2 = new HourAngle(hour, new MinuteAngle(minute))

        if (hourAns2.getHour() != -1 & & hourAns2.getMinuteAngle().getMinute() != -1) {
            float calcHourAns = hourAngle.getAngle()
            float calcMinsAns = hourAngle.getMinuteAngle().getAngle()
            float result = Math.abs(calcHourAns - calcMinsAns)
            return Math.min(360 - result, result)
        } else {
            return -1
        }
    }
    }

    public class Main {
    public static void main(String[] args) {
        int[] ls
        if (args.length > 0) {
            ls = Clock.readFromFile(args[0])
        } else {
            ls = Clock.readFromFile("exercise4.txt")
        }

        if (ls.length > 0 & & ls[0] != -1) {
            MinuteAngle minuteAns = new MinuteAngle(ls[1])
            HourAngle hourAns = new HourAngle(ls[0], minuteAns)
            Clock clock = new Clock(hourAns)
            float ans = clock.calcAngle()
            if (ans != -1) {
                System.out.println(
                    "Angle between hour hand and minute hand is: " + ans)
            } else {
                System.out.println(
                    "Don't have value of angle between hour hand and minute hand")
            }
        } else {
            System.out.println(
                "Don't have value to calculate angle between two hand of clock")
        }
    }
}
