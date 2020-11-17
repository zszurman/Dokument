from tkinter import *
from doc import Doc
from lista import make_list_dok
from lista import make_list_cyf
from lista import make_list_bday
from lista import make_map
from bday import Bday


class Application:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x1000")
        self.root.title("Moje dokumenty")
        self.root.config(padx=5, pady=5, bg="#000033")
        self.make_window()
        self.root.mainloop()

    def make_window(self):

        Label(text="Dokumenty", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=3, sticky=W)
        Label(text="Urodziny i Rocznice", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=1, sticky=W)
        Label(text="Cyferki", bg="#000033", fg="#F0FF62", font=("Calibri", 16), padx=40, pady=5) \
            .grid(row=0, column=5, sticky=W)

        dok = make_list_dok()
        dok.sort(key=Doc.sort_time)
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
            Label(text=dok[i].interval_short, bg="#000033", fg="#F0FF62", font=("Calibri", 12), padx=40, pady=5) \
                .grid(row=i + 1, column=3, sticky=W)
            i += 1

        rodz = make_list_bday()
        rodz.sort(key=Bday.sort_time)
        i = 0
        while i < len(rodz):
            photo = PhotoImage(file=rodz[i].im())
            w = Label(image=photo)
            w.photo = photo
            w.grid(row=i + 1, column=0)
            Label(text=rodz[i].short_str(), bg="#000033", fg="#F0FF62", font=("Calibri", 12), padx=40, pady=5) \
                .grid(row=i + 1, column=1, sticky=W)
            i += 1

        cyf = make_list_cyf()
        i = 0
        while i < len(cyf):
            photo = PhotoImage(file=cyf[i].icon)
            w = Label(image=photo)
            w.photo = photo
            w.grid(row=i + 1, column=4)

            com = self.but0
            if i == 0:
                com = self.but0
            if i == 1:
                com = self.but1
            if i == 2:
                com = self.but2
            if i == 3:
                com = self.but3
            if i == 4:
                com = self.but4
            if i == 5:
                com = self.but5
            if i == 6:
                com = self.but6
            if i == 7:
                com = self.but7
            if i == 8:
                com = self.but8
            if i == 9:
                com = self.but9
            if i == 10:
                com = self.but10
            if i == 11:
                com = self.but11
            if i == 12:
                com = self.but12
            if i == 13:
                com = self.but13
            if i == 14:
                com = self.but14
            if i == 15:
                com = self.but15

            Button(text=cyf[i].name, bg="#000033", fg="#F0FF62", width=20, font=("Calibri", 12), padx=40, pady=5,
                   command=com).grid(row=i + 1, column=5, sticky=W)
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
    def but(i):
        cyf = make_list_cyf()
        root = Tk()
        root.geometry("600x200")
        root.title(cyf[i].name)
        root.config(padx=5, pady=5)
        t = Text(root, width=15, height=70, wrap=NONE, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 14), padx=20, pady=5)
        t.insert(END, str(cyf[i]) + "\n")
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        root.mainloop()

    def but0(self):
        self.but(0)

    def but1(self):
        self.but(1)

    def but2(self):
        self.but(2)

    def but3(self):
        self.but(3)

    def but4(self):
        self.but(4)

    def but5(self):
        self.but(5)

    def but6(self):
        self.but(6)

    def but7(self):
        self.but(7)

    def but8(self):
        self.but(8)

    def but9(self):
        self.but(9)

    def but10(self):
        self.but(10)

    def but11(self):
        self.but(11)

    def but12(self):
        self.but(12)

    def but13(self):
        self.but(13)

    def but14(self):
        self.but(14)

    def but15(self):
        self.but(15)

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
