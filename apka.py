from tkinter import *
from klasa import Doc
from lista import make_list


class Application:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x1000")
        self.root.title("Moje dokumenty")
        self.root.config(padx=5, pady=5, bg="#000033")
        self.make_window()
        self.root.mainloop()

    def make_window(self):

        dok = make_list()
        dok.sort(key=Doc.sort_time)

        i = 0
        while i < len(dok):
            Label(text=dok[i].short(), bg="#000033", fg="#F0FF62", font=("Calibri", 12)) \
                .grid(row=i, column=0, sticky=W)
            i += 1

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Najbliższe", command=self.near)
        filemenu.add_command(label="Najdalsze", command=self.far)
        filemenu.add_separator()
        filemenu.add_command(label="Alfabetycznie +", command=self.alfa)
        filemenu.add_command(label="Alfabetycznie -", command=self.omega)
        filemenu.add_separator()
        filemenu.add_command(label="Zakończ", command=self.root.destroy)
        menubar.add_cascade(label="Zobacz szczegóły", menu=filemenu)
        self.root.config(menu=menubar)

    @staticmethod
    def near():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Najbliższe")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#FFFFCC", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list()
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
    def far():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Najdalsze")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#E5FFCC", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list()
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
    def alfa():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Alfabetycznie +")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#CCFFFF", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list()
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
    def omega():
        kot = Tk()
        kot.geometry("600x700")
        kot.title("Alfabetycznie -")
        kot.config(padx=5, pady=5)
        v = Scrollbar(kot)
        v.pack(side=RIGHT, fill=Y)
        t = Text(kot, width=15, height=70, wrap=NONE, yscrollcommand=v.set, bg="#D6F2D9", fg="#000066",
                 font=("Calibri", 12), padx=20, pady=5)
        dok = make_list()
        dok.sort(key=Doc.sort_name, reverse=True)

        i = 0
        while i < len(dok):
            t.insert(END, str(dok[i]) + "\n")
            i += 1

        t.pack(side=TOP, fill=X)
        t.configure(state='disabled')
        v.config(command=t.yview)
        kot.mainloop()


Application()
