class MyTime:

    def __int__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes + 60 + hours * 60 * 60
    def __eq__(self, other) -> bool:
        return self.timestamp == other.timestamp

if __name__ == "__main__":
    time1 = MyTime(12, 12, 12)
    time2 = MyTime(12, 12, 12)
    print(time1 == time2)


