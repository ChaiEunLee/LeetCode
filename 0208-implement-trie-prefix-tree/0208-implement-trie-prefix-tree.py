import collections
class TrieNode:
    def __init__(self):
        self.word = False #각자의 노드는 word 값을 가지고, 이 값은 단어가 모두 완성되었을 때만 True가 됨.(leaf만 True임)
        self.children = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char] #a->p->p->... 각 노드의 children으로 다음 알파벳을 노드로 붙임.
        node.word = True #leaf node에 True
 
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)