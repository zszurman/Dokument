class Cyf:
    def __init__(self, name, info1, info2, icon):
        self.name = name
        self.info1 = info1
        self.info2 = info2
        self.icon = icon

    def __str__(self):
        return str(self.name) + "\n" + str(self.info1) + "\n" + str(self.info2) + "\n"