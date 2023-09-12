import numpy as np
import random
import os

from .Player import Player
from .fileReaderForRoulette import fileReaderForRoulette


class Roulette:
    def __init__(self, names: list, checkedList: list):
        self.checkedPlayers, self.uncheckedPlayers = self.__makePlayersListFromNames(names, checkedList)

        self.__lastIndex = -1

        seedSize = 10
        seed = os.urandom(seedSize)
        random.seed(seed)

    @classmethod
    def fromFile(cls, fileName):

        names, checkedList = fileReaderForRoulette.readNamesAndCheckedListFromFile(fileName)

        return cls(names, checkedList)

    def spin(self) -> int:
        if len(self.uncheckedPlayers) < 1:
            raise Exception('All players checked')

        self.__lastIndex = random.randint(1, len(self.uncheckedPlayers)) - 1

        return self.__lastIndex

    def shot(self, index: int = -1) -> str:
        pick = self.uncheckedPlayers[self.__lastIndex]

        if (pick.checked):
            raise Exception('Picked player is already checked')

        self.uncheckedPlayers = np.delete(self.uncheckedPlayers, self.__lastIndex)
        pick.checked = True
        self.checkedPlayers = np.append(self.checkedPlayers, [pick])

        return pick.name

    def spinAndShot(self):
        try:
            self.spin()
            return self.shot()
        except Exception as e:
            raise Exception('All players checked')

    def getCheckedPlayersCount(self) -> int:
        return len(self.checkedPlayers)
    

    def getUncheckedPlayersCount(self) -> int:
        return len(self.uncheckedPlayers)
    

    def getPlayersCount(self) -> int:
        return self.getCheckedPlayersCount() + self.getUncheckedPlayersCount()

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

    def __makePlayersListFromNames(self, names: list, checkedList: list = []) -> [np.array, np.array]:
        self.__fillCheckedList(checkedList, len(names))

        checked = [Player(name, check) for name, check in zip(names, checkedList) if check]
        unchecked = [Player(name, check) for name, check in zip(names, checkedList) if not check]

        return np.array(checked), np.array(unchecked)

    def __fillCheckedList(self, checkedList: list, size: int) -> np.array:
        i = len(checkedList)
        while i < size:
            checkedList.append(False)
            i += 1
        return np.array(checkedList)