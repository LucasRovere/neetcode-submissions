class Trie:
    class Node:
        def __init__(self, isWord):
            self.isWord = isWord
            self.children = {}
        
        def getChild(self, val, isWord):
            if val not in self.children:
                self.children[val] = Trie.Node(isWord)
                return self.children[val]
            else:
                if isWord != None:
                    self.children[val].isWord = isWord
                return self.children[val]

    def __init__(self):
        self.root = self.Node(False)

    def addWord(self, word):
        cur = self.root
        for c in word[:-1]:
            cur = cur.getChild(c, None)
        cur.getChild(word[-1], True)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def toRef(pos):
            return pos[0] + pos[1]*n

        def toPos(node):
            return (node % n, node // n)

        def nextPos(pos, curVisited):
            valid = set()
            if pos[0] > 0:
                valid.add((pos[0] - 1, pos[1]))
            if pos[0] < n-1:
                valid.add((pos[0] + 1, pos[1]))
            if pos[1] > 0:
                valid.add((pos[0], pos[1] - 1))
            if pos[1] < m-1:
                valid.add((pos[0], pos[1] + 1))

            return valid - curVisited

        def checkPos(pos, curVisited, node, partial):
            c = board[pos[0]][pos[1]]
            ref = toRef(pos)
            found = set()
            # print(pos, c)
            # print(partial)
            # print(node.isWord)

            if c not in starters and ref in toCheck:
                toCheck.remove(ref)

            if c not in node.children:
                return found

            node = node.children[c]                
            curVisited.add(pos)
            partial += c
            
            if node.isWord:
                found.add(partial)

            for np in nextPos(pos, curVisited):
                newFound = checkPos(np, curVisited, node, partial)
                found = found.union(newFound)

            curVisited.remove(pos)
            return found

        n = len(board)
        m = len(board[0])
        toCheck = set(range(n*m))
        trie = Trie()
        starters = trie.root.children.keys()

        for word in words:
            trie.addWord(word)

        found = set()
        while toCheck:
            ref = toCheck.pop()
            pos = toPos(ref)
            newFound = checkPos(pos, set(), trie.root, "")
            found = found.union(newFound)

        return list(found)
