class PrefixTreeNode:
    def __init__(self):
        self.childs = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        self.__runPath(word, True)

    def search(self, word: str) -> bool:
        finalNode = self.__runPath(word, False)

        if finalNode == None:
            return False
        else:
            return finalNode.isWord
        

    def startsWith(self, prefix: str) -> bool:
        finalNode = self.__runPath(prefix, False)
        return finalNode != None


    def __runPath(self, path, addMissing):
        nextNode = self.root
        last = len(path) - 1

        for i, c in enumerate(path):
            if c in nextNode.childs:
                nextNode = nextNode.childs[c]
            elif addMissing:
                newNode = PrefixTreeNode()
                nextNode.childs[c] = newNode
                nextNode = newNode
            else:
                return None

            if i == last:
                if addMissing:
                    nextNode.isWord = True
                return nextNode
        
        