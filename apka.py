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
            Label(text=cyf[i].name, bg="#000033", fg="#F0FF62", font=("Calibri", 12), padx=40, pady=5) \
                .grid(row=i + 1, column=5, sticky=W)
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
        dok_menu.add_command(label="Cyferki", command=self.cyferki)
        dok_menu.add_separator()
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
    def near_r():
        kot = Tk()
        kot.geometry("400x500")
        kot.title("Najbliższe urodziny i rocznice")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 11), padx=20, pady=5)
        rodzinka = make_list_bday()
        rodzinka.sort(key=Bday.sort_time)
        i = 0
        while i < len(rodzinka):
            t.insert(END, str(rodzinka[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def far_r():
        kot = Tk()
        kot.geometry("400x500")
        kot.title("Najdalsze urodziny i rocznice")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#E5FFCC", fg="#000066",
                 font=("Calibri", 10), padx=20, pady=5)
        rodzinka = make_list_bday()
        rodzinka.sort(key=Bday.sort_time, reverse=True)
        i = 0
        while i < len(rodzinka):
            t.insert(END, str(rodzinka[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def young_r():
        kot = Tk()
        kot.geometry("400x500")
        kot.title("Najmłodsi i najmłodsze rocznice")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#F2DBF6", fg="#000066",
                 font=("Calibri", 11), padx=20, pady=5)
        rodzinka = make_list_bday()
        rodzinka.sort(key=Bday.sort_old, reverse=True)
        i = 0
        while i < len(rodzinka):
            t.insert(END, str(rodzinka[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def old_r():
        kot = Tk()
        kot.geometry("400x500")
        kot.title("Najstarsi i najstarsze rocznice")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#E0E0E0", fg="#000066",
                 font=("Calibri", 11), padx=20, pady=5)
        rodzinka = make_list_bday()
        rodzinka.sort(key=Bday.sort_old)
        i = 0
        while i < len(rodzinka):
            t.insert(END, str(rodzinka[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def alfa_r():
        kot = Tk()
        kot.geometry("400x500")
        kot.title("Alfabetycznie +")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#CCFFFF", fg="#000066",
                 font=("Calibri", 11), padx=20, pady=5)
        rodzinka = make_list_bday()
        rodzinka.sort(key=Bday.sort_surname)
        i = 0
        while i < len(rodzinka):
            t.insert(END, str(rodzinka[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def omega_r():
        kot = Tk()
        kot.geometry("400x500")
        kot.title("Alfabetycznie -")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#D6F2D9", fg="#000066",
                 font=("Calibri", 11), padx=20, pady=5)
        rodzinka = make_list_bday()
        rodzinka.sort(key=Bday.sort_surname, reverse=True)
        i = 0
        while i < len(rodzinka):
            t.insert(END, str(rodzinka[i]) + "\n")
            i += 1
        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def cyferki():
        kot = Tk()
        kot.geometry("700x800")
        kot.title("Cyferki")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 14), padx=20, pady=5)
        cyf = make_list_cyf()

        i = 0
        while i < len(cyf):
            t.insert(END, str(cyf[i]) + "\n")
            i += 1

        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def near_d():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Najbliższe")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list_dok()
        dok.sort(key=Doc.sort_time)

        i = 0
        while i < len(dok):
            t.insert(END, str(dok[i]) + "\n")
            i += 1

        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def far_d():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Najdalsze")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#E5FFCC", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list_dok()
        dok.sort(key=Doc.sort_time, reverse=True)

        i = 0
        while i < len(dok):
            t.insert(END, str(dok[i]) + "\n")
            i += 1

        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def alfa_d():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Alfabetycznie +")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#CCFFFF", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list_dok()
        dok.sort(key=Doc.sort_name)

        i = 0
        while i < len(dok):
            t.insert(END, str(dok[i]) + "\n")
            i += 1

        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

    @staticmethod
    def omega_d():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Alfabetycznie -")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#D6F2D9", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list_dok()
        dok.sort(key=Doc.sort_name, reverse=True)

        i = 0
        while i < len(dok):
            t.insert(END, str(dok[i]) + "\n")
            i += 1

        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()

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
