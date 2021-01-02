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

    def clear_list(self):
        y2 = datetime.datetime.now()
        y1 = datetime.datetime(y2.year, y2.month, y2.day)
        y = y1.timestamp()
        L = self.daty
        for element in L:
            x1 = datetime.datetime.strptime(element, "%d.%m.%Y")
            x = x1.timestamp()
            dx = x - y
            if dx < 0:
                L.remove(element)
                self.clear_list()
        return L

    def find_day(self):
        L = self.clear_list()
        y2 = datetime.datetime.now()
        y1 = datetime.datetime(y2.year, y2.month, y2.day)
        y = y1.timestamp()
        x1 = datetime.datetime.strptime(L[0], "%d.%m.%Y")
        x = x1.timestamp()
        return int((x - y) / (60 * 60 * 24))

    def find_date(self):
        L = self.clear_list()
        x = datetime.datetime.strptime(L[0], "%d.%m.%Y")
        mc = self.polish_month(x.month)
        day = str(x.day)
        week = self.polish_day(x.weekday())
        return f"{day} {mc} ({week})"

    def str1(self):
        dni = "dni"
        if self.find_day() == 1:
            dni = "dzień"
        if self.find_day() > 0:
            return f"{self.name} za {self.find_day()} {dni} {self.find_date()}"
        elif self.find_day() == 0:
            return f"{self.name} dzisiaj {self.find_date()}"
        else:
            return f"{self.name} w tym roku koniec"

    def print_list(self):
        L = self.clear_list()
        i = 0
        text = "Pozostałe dni:  "
        while i < len(L):
            if i == len(L) - 1:
                text += f"{L[i]}\n"
            elif i == 2 or i == 7 or i == 11:
                text += f"{L[i]},\n"
            else:
                text += f"{L[i]},   "
            i += 1
        return text

    def __str__(self):
        return f"{self.print_list()}\n{self.info}"
