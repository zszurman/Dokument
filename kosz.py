import datetime


class Kosz:
    def __init__(self, name, daty, info, image):
        self.name = name
        self.daty = daty
        self.info = info
        self.image = image

    @staticmethod
    def polish_day(dt):
        if dt == 0:
            y = "poniedziałek"
        elif dt == 1:
            y = "wtorek"
        elif dt == 2:
            y = "środa"
        elif dt == 3:
            y = "czwartek"
        elif dt == 4:
            y = "piątek"
        elif dt == 5:
            y = "sobota"
        elif dt == 6:
            y = "niedziela"
        else:
            y = "błąd dnia"
        return y

    @staticmethod
    def polish_month(mc):
        if mc == 1:
            y = " stycznia "
        elif mc == 2:
            y = " lutego "
        elif mc == 3:
            y = " marca "
        elif mc == 4:
            y = " kwietnia "
        elif mc == 5:
            y = " maja "
        elif mc == 6:
            y = " czerwca "
        elif mc == 7:
            y = " lipca "
        elif mc == 8:
            y = " sierpnia "
        elif mc == 9:
            y = " września "
        elif mc == 10:
            y = " października "
        elif mc == 11:
            y = " listopada "
        elif mc == 12:
            y = " grudnia "
        else:
            y = "błąd m-ca"
        return y

    def find_index(self):
        y2 = datetime.datetime.now()
        y1 = datetime.datetime(y2.year, y2.month, y2.day)
        y = y1.timestamp()
        i = 0
        my_index = 0
        while i < len(self.daty):
            x1 = datetime.datetime.strptime(self.daty[i], "%d.%m.%Y")
            x = x1.timestamp()
            dx = int((x - y) / (60 * 60 * 24))
            if dx >= 0:
                my_index = i
                break
            i += 1
        return my_index

    def find_day(self):
        y2 = datetime.datetime.now()
        y1 = datetime.datetime(y2.year, y2.month, y2.day)
        y = y1.timestamp()
        x1 = datetime.datetime.strptime(self.daty[self.find_index()], "%d.%m.%Y")
        x = x1.timestamp()
        return int((x - y) / (60 * 60 * 24))

    def find_date(self):
        x = datetime.datetime.strptime(self.daty[self.find_index()], "%d.%m.%Y")
        mc = self.polish_month(x.month)
        day = str(x.day)
        week = self.polish_day(x.weekday())
        return day + mc + "(" + week + ")"

    def str1(self):
        dni = " dni "
        if self.find_day() == 1:
            dni = " dzień "
        if self.find_day() > 0:
            return str(self.name) + " za " + str(self.find_day()) + dni + str(self.find_date())
        elif self.find_day() == 0:
            return str(self.name) + " dzisiaj " + str(self.find_date())
        else:
            return str(self.name) + " w tym roku koniec"

    def __str__(self):
        return self.info
