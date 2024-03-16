class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # beginword -> endword로 가는데 한글자씩 바꿔서 도달
        alphabet = "abcdefghijklmnopqrstuvwxyz" 
        queue = [(beginWord,1)]
        wordList = set(wordList)
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for k in alphabet:
                    newword = word[:i] + k + word[i+1:]
                    if newword in wordList:
                        wordList.remove(newword)
                        queue.append((newword, length+1))
        return 0