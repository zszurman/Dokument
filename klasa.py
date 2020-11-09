import datetime


class Doc:
    def __init__(self, name, date, info1, info2):
        self.name = name
        self.date = date
        self.info1 = info1
        self.info2 = info2

    @property
    def interval(self):
        day1 = datetime.datetime.strptime(self.date, "%d.%m.%Y")
        x1 = day1.timestamp()

        y = datetime.datetime.now()
        day2 = datetime.datetime(y.year, y.month, y.day)
        x2 = day2.timestamp()

        dx = int((x1 - x2) / (60 * 60 * 24))
        dy = int(dx // 365.25)
        dd = int(dx % 365.25)

        str1 = " dni "
        if dd == 1:
            str1 = " dzień "

        str2 = " lat i "
        if dy == 1 or dy == -1:
            str2 = " rok i "
        if (2 <= dy % 10 <= 4) and (dy < 10 or dy > 20):
            str2 = " lata i "
        if dy == -2 or dy == -3 or dy == -4:
            str2 = " lata i "

        str3 = " (do " + self.date + ")"

        if dy == 0:
            return str(dx) + str1 + str3
        elif dy > 30:
            return ""
        elif dx < 0:
            return "termin upłynął " + self.date
        else:
            return str(dy) + str2 + str(dd) + str1 + str3

    def sort_time(self):
        x = datetime.datetime.strptime(self.date, "%d.%m.%Y")
        return x.timestamp()

    def sort_name(self):
        return self.name

    def __str__(self):
        return str(self.name) + "\n" \
               + str(self.info1) + "\n" \
               + str(self.info2) + "\n" \
               + str(self.interval) + "\n"

    def short(self):
        return str(self.name) + "     " + str(self.interval)
