

class fileReaderForRoulette:
    def __init__(self):
        raise Exception('Unaible to create objects of this class')

    @classmethod
    def readNamesAndCheckedListFromFile(cls, fileName):
        file = open(fileName, 'r')
        names = []
        checkedList = []

        for line in file:
            n, c = line.split('-')
            names.append(n.strip(' \n'))
            checkedList.append(cls.strToBool(c.strip(' \n')))

        file.close()

        return names, checkedList

    def strToBool(s: str) -> bool:
        return s == '1' or s == 'True' or s == 'true'