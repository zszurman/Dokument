import datetime


class Bday:
    def __init__(self, name, surname, r, m, d, tel, home, mail, typ, image):
        self.name = name
        self.surname = surname
        self.r = r
        self.m = m
        self.d = d
        self.tel = tel
        self.address = home
        self.mail = mail
        self.typ = typ
        self.image = image

    def im(self):
        return str(self.image)

    def sort_time(self):
        now = datetime.date.today()
        yd_now = now.timetuple().tm_yday

        uro = datetime.date(now.year, self.m, self.d)
        yd_uro = uro.timetuple().tm_yday

        uro_new = datetime.date(now.year + 1, self.m, self.d)
        yd_uro_new = uro_new.timetuple().tm_yday

        syl = datetime.date(now.year, 12, 31)
        yd_syl = syl.timetuple().tm_yday

        if yd_uro > yd_now:
            dni = yd_uro - yd_now
        elif yd_uro == yd_now:
            dni = 0
        else:
            dni = yd_syl - yd_now + yd_uro_new
        return dni

    def sort_old(self):
        return datetime.date(self.r, self.m, self.d)

    def sort_surname(self):
        return self.surname + " " + self.name + "\n"

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
            y = " styczeń "
        elif mc == 2:
            y = " luty "
        elif mc == 3:
            y = " marzec "
        elif mc == 4:
            y = " kwiecień "
        elif mc == 5:
            y = " maj "
        elif mc == 6:
            y = " czerwiec "
        elif mc == 7:
            y = " lipiec "
        elif mc == 8:
            y = " sierpień "
        elif mc == 9:
            y = " wrzesień "
        elif mc == 10:
            y = " październik "
        elif mc == 11:
            y = " listopad "
        elif mc == 12:
            y = " grudzień "
        else:
            y = "błąd m-ca"
        return y

    def introduce(self):
        if self.typ == "u":
            return str(self.name) + " " + str(self.surname) + "\n" \
                   + self.address + "\nTel.: " + self.tel + "\nEmail: " + self.mail + "\n"
        else:
            return str(self.name) + " " + str(self.surname) + "\n" + self.address + "\n"

    def born_day(self):
        born = datetime.date(self.r, self.m, self.d)
        week_day = born.weekday()
        tyt = "Data urodzenia: "
        if self.typ == "r":
            tyt = "Data ślubu: "

        return tyt + str(self.d) + str(self.polish_month(self.m)) + str(self.r) + " (" + self.polish_day(
            week_day) + ")\n"

    def calculate_age(self):
        born = datetime.date(self.r, self.m, self.d)
        now = datetime.date.today()
        yd_now = now.timetuple().tm_yday
        uro = datetime.date(now.year, self.m, self.d)
        yd_uro = uro.timetuple().tm_yday
        uro_old = datetime.date(now.year - 1, self.m, self.d)
        yd_uro_old = uro_old.timetuple().tm_yday
        syl_old = datetime.date(now.year - 1, 12, 31)
        yd_syl_old = syl_old.timetuple().tm_yday

        w = "Wiek: "
        y = "Dzisiaj kończy "
        if self.typ == "r":
            w = "Po ślubie: "
            y = "Dziś Rocznica Ślubu "

        if yd_uro < yd_now:
            lat = now.year - born.year
            dni = yd_now - yd_uro
        elif yd_uro == yd_now:
            lat = now.year - born.year
            dni = 0
        else:
            lat = now.year - born.year - 1
            dni = yd_syl_old - yd_uro_old + yd_now

        str_lat = " lat i "
        if lat == 1:
            str_lat = " rok i "
        elif (lat % 10 > 1) and (lat % 10 < 5) and (lat > 20 or lat < 10):
            str_lat = " lata i "

        if dni == 0:
            return y + str(lat) + " rok\n"
        elif dni == 1:
            return w + str(lat) + str_lat + str(dni) + " dzień\n"
        else:
            return w + str(lat) + str_lat + str(dni) + " dni\n"

    def calculate_time(self):
        now = datetime.date.today()
        yd_now = now.timetuple().tm_yday

        uro = datetime.date(now.year, self.m, self.d)
        yd_uro = uro.timetuple().tm_yday

        uro_new = datetime.date(now.year + 1, self.m, self.d)
        yd_uro_new = uro_new.timetuple().tm_yday

        syl = datetime.date(now.year, 12, 31)
        yd_syl = syl.timetuple().tm_yday

        if yd_uro > yd_now:
            dni = yd_uro - yd_now
            week_day = uro.weekday()
        elif yd_uro == yd_now:
            dni = 0
            week_day = uro_new.weekday()
        else:
            dni = yd_syl - yd_now + yd_uro_new
            week_day = uro_new.weekday()

        rz = "Następne urodziny dokładnie za rok ("
        y = "Urodziny za 1 dzień ("
        z = "Urodziny za "
        if self.typ == "r":
            rz = "Następna rocznica za dokładnie za rok ("
            y = "Rocznica za 1 dzień ("
            z = "Rocznica za "

        if dni == 0:
            return rz + self.polish_day(week_day) + ")"
        elif dni == 1:
            return y + self.polish_day(week_day) + ")"
        else:
            return z + str(dni) + " dni (" + self.polish_day(week_day) + ")"

    def __str__(self):
        return self.introduce() + self.born_day() + self.calculate_age() + self.calculate_time() + "\n"

    def short_str(self):
        if self.sort_time() == 0:
            return "     Dzisiaj   " + self.name + " " + self.surname
        elif self.sort_time() == 1:
            return "     Jutro   " + self.name + " " + self.surname
        elif self.sort_time() == 2:
            return "     Pojutrze   " + self.name + " " + self.surname
        else:
            return "     Za " + str(self.sort_time()) + " dni   " + self.name + " " + self.surname
