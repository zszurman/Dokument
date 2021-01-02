class Cyf:
    def __init__(self, name, info1, info2, icon):
        self.name = name
        self.info1 = info1
        self.info2 = info2
        self.icon = icon

    def __str__(self):
        return f"{self.name}\n{self.info1}\n{self.info2}\n"

    def sort_name(self):
        return f"{self.name}"



