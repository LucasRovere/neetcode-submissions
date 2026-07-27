class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordLen = len(beginWord)
        paths = [[beginWord]]
        remaining = set(wordList)
        found = None
        c = 0

        if endWord not in remaining:
            return 0

        if beginWord in remaining:
            remaining.remove(beginWord)

        while len(remaining) > 0 and not found:
            c += 1
            print("Rem", remaining)
            newPaths = []
            allMatches = set()

            for path in paths:
                print("Path", path, len(paths))
                matches = set()
                lastWord = path[-1]
                # print("Last", lastWord)

                for checkWord in remaining:
                    # print("Check", checkWord)

                    diff = 0
                    for i in range(wordLen):
                        if lastWord[i] != checkWord[i]:
                            diff += 1
                            if diff > 1:
                                break
                    
                    if diff == 1:
                        matches.add(checkWord)

                        if checkWord == endWord:
                            return len(path) + 1

                for match in matches:
                    newPath = path + [match]
                    newPaths.append(newPath)

                allMatches = allMatches.union(matches)
            
            remaining = remaining - allMatches

            print(newPaths)
            if not newPaths:
                break
            paths = newPaths
            
        # if not found:
        return 0

        # return len(found)
        