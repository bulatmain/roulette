

class fileReaderForRoulette:
    def __init__(self):
        raise Exception('Unaible to create objects of this class')

    @classmethod
    def readNamesAndCheckedListFromFile(cls, fileName):
        file = open(fileName, 'r')
        names = []
        checkedList = []

        for line in file:
            try:
                n, c = line.split('-')
                n = n.strip(' \n')
                c = c.strip(' \n')
                names.append(n)
                checkedList.append(cls.strToBool(c))
            except Exception  as e:
                n = line.strip(' \n')
                names.append(n)
                checkedList.append(False)


        file.close()

        return names, checkedList

    def strToBool(s: str) -> bool:
        return s == '1' or s == 'True' or s == 'true'