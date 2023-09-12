
class Player:
    def __init__(self, name: str, checked: bool = False):
        self.name = name
        self.checked = checked

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + ' - ' + str(self.checked)