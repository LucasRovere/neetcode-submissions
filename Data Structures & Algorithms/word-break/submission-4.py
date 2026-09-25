class Solution:
    class Trie:
        def __init__(self):
            root = { "is_word": False, "letters": {} }
            self.nodes = [root]

        def addWord(self, word):
            next_node = self.nodes[0]
            
            for c in word:
                if c not in next_node["letters"]:
                    self.nodes.append({ "is_word": False, "letters": {} })
                    next_node["letters"][c] = len(self.nodes) - 1

                next_node = self.nodes[next_node["letters"][c]]

            next_node["is_word"] = True

        def findTarget(self, target):
            self.seen = [False] * len(target)

            return self.partialWords(target)

        def partialWords(self, word):
            if self.seen[len(word) - 1]:
                return False

            # print("Called with", word)
            next_node = self.nodes[0]
            result = []
            current = ""

            for c in word:
                # print("-", c)
                if next_node["is_word"]:
                    # print("- is_word", current)
                    result.append(current)
                    if current == word:
                        return True
                if c in next_node["letters"]:
                    # print("- has next")
                    next_node = self.nodes[next_node["letters"][c]]
                    current = current + c
                else:
                    # print("- no next")
                    next_node = None
                    break

            if next_node and next_node["is_word"]:
                # print("- is_word", current)
                result.append(current)
                if current == word:
                    return True

            # print("results", result[::-1])
            for r in result[::-1]:
                n = len(r)
                if self.partialWords(word[n:]):
                    return True
            
            self.seen[len(word)-1] = True
            return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = self.Trie()

        for word in wordDict:
            trie.addWord(word)

        return trie.findTarget(s)
        