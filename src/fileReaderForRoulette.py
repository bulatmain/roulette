

class fileReaderForRoulette:
    names = []
    checkedList = []

    def __init__(self):
        raise Exception('Unaible to create objects of this class')

    @classmethod
    def readNamesAndCheckedListFromFile(cls, fileName):
        file = open(fileName, 'r')

        for line in file:
            cls.parseAndAppendLine(line)

        file.close()

        return cls.names, cls.checkedList
    
    @classmethod
    def parseAndAppendLine(cls, line):
        try:
            n, c = line.split('-')
            n = n.strip(' \n')
            c = cls.strToBool(c.strip(' \n'))
        except Exception as e:
            n = line.strip(' \n')
            c = False
        
        cls.names.append(n)
        cls.checkedList.append(c)


    def strToBool(s: str) -> bool:
        return s == '1' or s == 'True' or s == 'true'