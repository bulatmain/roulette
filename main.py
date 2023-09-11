import numpy as np
import random
import time
import itertools


class Player:
    def __init__(self, name: str, checked: bool = False):
        self.name = name
        self.checked = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + ' - ' + str(self.checked)

class Roulette:
    def __init__(self, names: list, checkedList: list):
        self.checkedPlayers, self.uncheckedPlayers = self.__makePlayersListFromNames(names, checkedList)

        self.checkedPlayersCount = len(self.checkedPlayers)
        self.uncheckedPlayersCount = len(self.uncheckedPlayers)
        self.playersCount = self.checkedPlayersCount + self.uncheckedPlayersCount

        mSeconds = round(time.time() * 1000)
        random.seed(mSeconds)

    @classmethod
    def fromFile(cls, fileName):
        file = open(fileName, 'r')
        names = []
        checkedList = []

        for line in file:
            n, c = line.split('-')
            names.append(n.strip(' \n'))
            checkedList.append(cls.strToBool(c.strip(' \n')))

        return cls(names, checkedList)


    def __makePlayersListFromNames(self, names: list, checkedList: list = []) -> [np.array, np.array]:
        self.fillCheckedList(checkedList, len(names))

        checked = [Player(name, check) for name, check in zip(names, checkedList) if check]
        unchecked = [Player(name, check) for name, check in zip(names, checkedList) if not check]

        return np.array(checked), np.array(unchecked)

    def strToBool(s: str) -> bool:
        return s == '1' or s == 'True' or s == 'true'

    def fillCheckedList(self, checkedList: list, size: int) -> np.array:
        i = len(checkedList)
        while i < size:
            checkedList.append(False)
            i += 1
        return np.array(checkedList)

    def spin(self) -> str:
        if len(self.uncheckedPlayers) < 1:
            return '\\All players checked\\'

        index = random.randint(1, len(self.uncheckedPlayers)) - 1
        pick = self.uncheckedPlayers[index]

        self.uncheckedPlayers = np.delete(self.uncheckedPlayers, index)
        pick.checked = True
        self.checkedPlayers = np.append(self.checkedPlayers, [pick])
        
        return pick.name

    def printChecked(self):
        for player in self.checkedPlayers:
            print(player.name)

    def printUnchecked(self):
        for player in self.uncheckedPlayers:
            print(player.name)

    def printPlayers(self):
        for player in self.checkedPlayers:
            print(player.name, '- checked')
        for player in self.uncheckedPlayers:
            print(player.name, '- unchecked')
        


roulette = Roulette.fromFile('namesFile')

for i in range(roulette.uncheckedPlayersCount):
    print(roulette.spin())

