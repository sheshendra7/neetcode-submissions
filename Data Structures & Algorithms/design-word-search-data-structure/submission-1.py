class TireNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.head = TireNode()

    def addWord(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = TireNode()
            cur = cur.child[ch]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            cur = root

            for i in range(j,len(word)):
                ch = word[i]
                if ch == '.':
                    for child in cur.child.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if ch not in cur.child:
                        return False
                    cur = cur.child[ch]
            return cur.endOfWord

        return dfs(0,self.head)