class WordDictionary:

    def __init__(self):
        self.children = [None]*26 #알파벳 26개
        self.isEndOfWord = False        

    def addWord(self, word: str) -> None:
        curr = self #현재를 self로 지정이 되네..?
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary() # 각 알파벳별로 각 알파벳이 들어있는 dict를 넣음
            curr = curr.children[ord(c) - ord('a')]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
            
            if curr.children[ord(c)-ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]
            
        return curr != None and curr.isEndOfWord
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)