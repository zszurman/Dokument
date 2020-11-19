from tkinter import *
from lista import *


class Application:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1600x1000")
        self.root.title("Moje dokumenty")
        self.root.config(padx=5, pady=5, bg="#000033")
        self.make_window()
        self.root.mainloop()

    def make_window(self):

        Label(text="Urodziny i Rocznice", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=1, sticky=W)
        Label(text="Dokumenty", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=3, sticky=W)
        Label(text="Cyferki", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=5, sticky=W)
        Label(text="Kalendarz", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=7, sticky=W)

        rodz = make_list_bday()
        rodz.sort(key=Bday.sort_time)
        list_ur = [self.ur0, self.ur1, self.ur2, self.ur3, self.ur4, self.ur5, self.ur6, self.ur7, self.ur8,
                   self.ur9, self.ur10, self.ur11, self.ur12, self.ur13, self.ur14, self.ur15, self.ur16, self.ur17,
                   self.ur18, self.ur19, self.ur20, self.ur21, self.ur22, self.ur23, self.ur24, self.ur25,
                   self.ur26, self.ur27, self.ur28, self.ur29, self.ur30, self.ur31
                   ]
        i = 0
        while i < len(rodz):
            photo = PhotoImage(file=rodz[i].im())
            w = Label(image=photo)
            w.photo = photo
            w.grid(row=i + 1, column=0)
            Button(text=rodz[i].short_str(), width=25, bg="#000033", fg="#F0FF62", font=("Calibri", 12), padx=40,
                   pady=5, command=list_ur[i]).grid(row=i + 1, column=1, sticky=W)
            i += 1

        dok = make_list_dok()
        dok.sort(key=Doc.sort_time)
        list_dut = [self.dut0, self.dut1, self.dut2, self.dut3, self.dut4, self.dut5, self.dut6, self.dut7, self.dut8,
                    self.dut9, self.dut10, self.dut11, self.dut12, self.dut13, self.dut14, self.dut15, self.dut16,
                    self.dut17, self.dut18, self.dut19, self.dut20, self.dut21, self.dut22, self.dut23
                    ]
        i = 0
        while i < len(dok):
            if dok[i].interval_int() < 0:
                photo = PhotoImage(file='drawable/ic_notok.png')
            elif dok[i].interval_int() < 31:
                photo = PhotoImage(file='drawable/ic_war.png')
            elif dok[i].interval_int() < 61:
                photo = PhotoImage(file='drawable/ic_war2.png')
            else:
                photo = PhotoImage(file='drawable/ic_ok.png')
            w = Label(image=photo)
            w.photo = photo
            w.grid(row=i + 1, column=2)
            Button(text=dok[i].interval_short, width=30, bg="#000033", fg="#F0FF62", font=("Calibri", 12), padx=40,
                   pady=5, command=list_dut[i]).grid(row=i + 1, column=3, sticky=W)
            i += 1

        cyf = make_list_cyf()
        cyf.sort(key=Cyf.sort_name)
        list_but = [self.but0, self.but1, self.but2, self.but3, self.but4, self.but5, self.but6, self.but7, self.but8,
                    self.but9, self.but10, self.but11, self.but12, self.but13, self.but14]
        i = 0
        while i < len(cyf):
            photo = PhotoImage(file=cyf[i].icon)
            w = Label(image=photo)
            w.photo = photo
            w.grid(row=i + 1, column=4)
            Button(text=cyf[i].name, bg="#000033", fg="#F0FF62", width=10, font=("Calibri", 12), padx=40, pady=5,
                   command=list_but[i]).grid(row=i + 1, column=5, sticky=W)
            i += 1

        kosz = make_list_kosz()
        kosz.sort(key=Kosz.find_day)
        list_kosz = [self.ko0, self.ko1, self.ko2, self.ko3, self.ko4, self.ko5, self.ko6]
        i = 0
        while i < len(kosz):
            photo = PhotoImage(file=kosz[i].image)
            w = Label(image=photo)
            w.photo = photo
            w.grid(row=i + 1, column=6)
            Button(text=kosz[i].str1(), bg="#000033", fg="#F0FF62", width=35, font=("Calibri", 12), padx=40, pady=5,
                   command=list_kosz[i]).grid(row=i + 1, column=7, sticky=W)
            i += 1

        menubar = Menu(self.root)

        rod_menu = Menu(menubar, tearoff=0)
        rod_menu.add_command(label="Najbliższe wydarzenia", command=self.near_r)
        rod_menu.add_command(label="Najdalsze wydarzenia", command=self.far_r)
        rod_menu.add_separator()
        rod_menu.add_command(label="Najmłodsze wydarzenia", command=self.young_r)
        rod_menu.add_command(label="Najstarsz wydarzenia", command=self.old_r)
        rod_menu.add_separator()
        rod_menu.add_command(label="Alfabetycznie +", command=self.alfa_r)
        rod_menu.add_command(label="Alfabetycznie -", command=self.omega_r)
        menubar.add_cascade(label="Urodziny i Rocznice", menu=rod_menu)

        dok_menu = Menu(menubar, tearoff=0)
        dok_menu.add_command(label="Najbliższe", command=self.near_d)
        dok_menu.add_command(label="Najdalsze", command=self.far_d)
        dok_menu.add_separator()
        dok_menu.add_command(label="Alfabetycznie +", command=self.alfa_d)
        dok_menu.add_command(label="Alfabetycznie -", command=self.omega_d)
        menubar.add_cascade(label="Dokumenty", menu=dok_menu)
        self.root.config(menu=menubar)

        map_menu = Menu(menubar, tearoff=0)
        map_menu.add_command(label="Czyżowice", command=self.map_cz)
        map_menu.add_command(label="Heilbronn", command=self.map_he)
        map_menu.add_command(label="Knurów", command=self.map_kn)
        map_menu.add_command(label="Gliwice", command=self.map_gl)
        map_menu.add_command(label="Bielsko-Biała", command=self.map_bi)
        map_menu.add_separator()
        map_menu.add_command(label="Dzierżoniów", command=self.map_dz)
        map_menu.add_command(label="Ściejowice", command=self.map_sc)
        map_menu.add_command(label="Niepołomice", command=self.map_ni)
        map_menu.add_command(label="Janowice", command=self.map_ja)
        map_menu.add_separator()
        map_menu.add_command(label="Europa", command=self.map_eu)
        menubar.add_cascade(label="Wyświetl mapy", menu=map_menu)

        menubar.add_cascade(label="Zakończ", command=self.root.destroy)

    @staticmethod
    def butt(i, make_list, sortuj):
        cyf = make_list
        cyf.sort(key=sortuj)
        root = Tk()
        root.geometry("600x250")
        root.title(cyf[i].name)
        root.config(padx=5, pady=5)
        t = Text(root, width=15, height=70, wrap=NONE, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 14), padx=20, pady=5)
        t.insert(END, str(cyf[i]) + "\n")
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        root.mainloop()

    def ur0(self):
        self.butt(0, make_list_bday(), Bday.sort_time)

    def ur1(self):
        self.butt(1, make_list_bday(), Bday.sort_time)

    def ur2(self):
        self.butt(2, make_list_bday(), Bday.sort_time)

    def ur3(self):
        self.butt(3, make_list_bday(), Bday.sort_time)

    def ur4(self):
        self.butt(4, make_list_bday(), Bday.sort_time)

    def ur5(self):
        self.butt(5, make_list_bday(), Bday.sort_time)

    def ur6(self):
        self.butt(6, make_list_bday(), Bday.sort_time)

    def ur7(self):
        self.butt(7, make_list_bday(), Bday.sort_time)

    def ur8(self):
        self.butt(8, make_list_bday(), Bday.sort_time)

    def ur9(self):
        self.butt(9, make_list_bday(), Bday.sort_time)

    def ur10(self):
        self.butt(10, make_list_bday(), Bday.sort_time)

    def ur11(self):
        self.butt(11, make_list_bday(), Bday.sort_time)

    def ur12(self):
        self.butt(12, make_list_bday(), Bday.sort_time)

    def ur13(self):
        self.butt(13, make_list_bday(), Bday.sort_time)

    def ur14(self):
        self.butt(14, make_list_bday(), Bday.sort_time)

    def ur15(self):
        self.butt(15, make_list_bday(), Bday.sort_time)

    def ur16(self):
        self.butt(16, make_list_bday(), Bday.sort_time)

    def ur17(self):
        self.butt(17, make_list_bday(), Bday.sort_time)

    def ur18(self):
        self.butt(18, make_list_bday(), Bday.sort_time)

    def ur19(self):
        self.butt(19, make_list_bday(), Bday.sort_time)

    def ur20(self):
        self.butt(20, make_list_bday(), Bday.sort_time)

    def ur21(self):
        self.butt(21, make_list_bday(), Bday.sort_time)

    def ur22(self):
        self.butt(22, make_list_bday(), Bday.sort_time)

    def ur23(self):
        self.butt(23, make_list_bday(), Bday.sort_time)

    def ur24(self):
        self.butt(24, make_list_bday(), Bday.sort_time)

    def ur25(self):
        self.butt(25, make_list_bday(), Bday.sort_time)

    def ur26(self):
        self.butt(26, make_list_bday(), Bday.sort_time)

    def ur27(self):
        self.butt(27, make_list_bday(), Bday.sort_time)

    def ur28(self):
        self.butt(28, make_list_bday(), Bday.sort_time)

    def ur29(self):
        self.butt(29, make_list_bday(), Bday.sort_time)

    def ur30(self):
        self.butt(30, make_list_bday(), Bday.sort_time)

    def ur31(self):
        self.butt(31, make_list_bday(), Bday.sort_time)

    def dut0(self):
        self.butt(0, make_list_dok(), Doc.sort_time)

    def dut1(self):
        self.butt(1, make_list_dok(), Doc.sort_time)

    def dut2(self):
        self.butt(2, make_list_dok(), Doc.sort_time)

    def dut3(self):
        self.butt(3, make_list_dok(), Doc.sort_time)

    def dut4(self):
        self.butt(4, make_list_dok(), Doc.sort_time)

    def dut5(self):
        self.butt(5, make_list_dok(), Doc.sort_time)

    def dut6(self):
        self.butt(6, make_list_dok(), Doc.sort_time)

    def dut7(self):
        self.butt(7, make_list_dok(), Doc.sort_time)

    def dut8(self):
        self.butt(8, make_list_dok(), Doc.sort_time)

    def dut9(self):
        self.butt(9, make_list_dok(), Doc.sort_time)

    def dut10(self):
        self.butt(10, make_list_dok(), Doc.sort_time)

    def dut11(self):
        self.butt(11, make_list_dok(), Doc.sort_time)

    def dut12(self):
        self.butt(12, make_list_dok(), Doc.sort_time)

    def dut13(self):
        self.butt(13, make_list_dok(), Doc.sort_time)

    def dut14(self):
        self.butt(14, make_list_dok(), Doc.sort_time)

    def dut15(self):
        self.butt(15, make_list_dok(), Doc.sort_time)

    def dut16(self):
        self.butt(16, make_list_dok(), Doc.sort_time)

    def dut17(self):
        self.butt(17, make_list_dok(), Doc.sort_time)

    def dut18(self):
        self.butt(18, make_list_dok(), Doc.sort_time)

    def dut19(self):
        self.butt(19, make_list_dok(), Doc.sort_time)

    def dut20(self):
        self.butt(20, make_list_dok(), Doc.sort_time)

    def dut21(self):
        self.butt(21, make_list_dok(), Doc.sort_time)

    def dut22(self):
        self.butt(22, make_list_dok(), Doc.sort_time)

    def dut23(self):
        self.butt(23, make_list_dok(), Doc.sort_time)

    def but0(self):
        self.butt(0, make_list_cyf(), Cyf.sort_name)

    def but1(self):
        self.butt(1, make_list_cyf(), Cyf.sort_name)

    def but2(self):
        self.butt(2, make_list_cyf(), Cyf.sort_name)

    def but3(self):
        self.butt(3, make_list_cyf(), Cyf.sort_name)

    def but4(self):
        self.butt(4, make_list_cyf(), Cyf.sort_name)

    def but5(self):
        self.butt(5, make_list_cyf(), Cyf.sort_name)

    def but6(self):
        self.butt(6, make_list_cyf(), Cyf.sort_name)

    def but7(self):
        self.butt(7, make_list_cyf(), Cyf.sort_name)

    def but8(self):
        self.butt(8, make_list_cyf(), Cyf.sort_name)

    def but9(self):
        self.butt(9, make_list_cyf(), Cyf.sort_name)

    def but10(self):
        self.butt(10, make_list_cyf(), Cyf.sort_name)

    def but11(self):
        self.butt(11, make_list_cyf(), Cyf.sort_name)

    def but12(self):
        self.butt(12, make_list_cyf(), Cyf.sort_name)

    def but13(self):
        self.butt(13, make_list_cyf(), Cyf.sort_name)

    def but14(self):
        self.butt(14, make_list_cyf(), Cyf.sort_name)

    def ko0(self):
        self.butt(0, make_list_kosz(), Kosz.find_day)

    def ko1(self):
        self.butt(1, make_list_kosz(), Kosz.find_day)

    def ko2(self):
        self.butt(2, make_list_kosz(), Kosz.find_day)

    def ko3(self):
        self.butt(3, make_list_kosz(), Kosz.find_day)

    def ko4(self):
        self.butt(4, make_list_kosz(), Kosz.find_day)

    def ko5(self):
        self.butt(5, make_list_kosz(), Kosz.find_day)

    def ko6(self):
        self.butt(6, make_list_kosz(), Kosz.find_day)

    @staticmethod
    def option_list(title, make_list, sort_key, revers):
        root = Tk()
        root.geometry("400x500")
        root.title(title)
        root.config(padx=5, pady=5)
        v = Scrollbar(root)
        v.pack(side=RIGHT, fill=Y)
        t = Text(root, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 11), padx=20, pady=5)
        lista = make_list
        lista.sort(key=sort_key, reverse=revers)
        i = 0
        while i < len(lista):
            t.insert(END, str(lista[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        root.mainloop()

    def near_r(self):
        self.option_list("Najbliższe urodziny i rocznice", make_list_bday(), Bday.sort_time, False)

    def far_r(self):
        self.option_list("Najdalsze urodziny i rocznice", make_list_bday(), Bday.sort_time, True)

    def young_r(self):
        self.option_list("Najmłodsi i najmłodsze rocznice", make_list_bday(), Bday.sort_old, True)

    def old_r(self):
        self.option_list("Najstarsi i najstarsze rocznice", make_list_bday(), Bday.sort_old, False)

    def alfa_r(self):
        self.option_list("Alfabetycznie +", make_list_bday(), Bday.sort_surname, False)

    def omega_r(self):
        self.option_list("Alfabetycznie -", make_list_bday(), Bday.sort_surname, True)

    def near_d(self):
        self.option_list("Najbliższe", make_list_dok(), Doc.sort_time, False)

    def far_d(self):
        self.option_list("Najdalsze", make_list_dok(), Doc.sort_time, True)

    def alfa_d(self):
        self.option_list("Alfabetycznie +", make_list_dok(), Doc.sort_name, False)

    def omega_d(self):
        self.option_list("Alfabetycznie -", make_list_dok(), Doc.sort_name, True)

    @staticmethod
    def map_cz():
        make_map(49.986, 18.42051, 17)

    @staticmethod
    def map_he():
        make_map(49.13556, 9.18322, 17)

    @staticmethod
    def map_kn():
        make_map(50.23069, 18.6626, 17)

    @staticmethod
    def map_gl():
        make_map(50.30197, 18.64435, 17)

    @staticmethod
    def map_bi():
        make_map(49.81506, 19.0283, 17)

    @staticmethod
    def map_dz():
        make_map(50.74028, 16.64504, 17)

    @staticmethod
    def map_sc():
        make_map(50.00158, 19.77959, 17)

    @staticmethod
    def map_ni():
        make_map(50.03111, 20.21154, 17)

    @staticmethod
    def map_ja():
        make_map(49.88891, 19.10136, 17)

    @staticmethod
    def map_eu():
        make_map(50, 15, 5)


Application()
