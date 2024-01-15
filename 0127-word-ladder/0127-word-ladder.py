class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        
        while queue:
            word, length = queue.popleft()
            #print("word, length : ", word, ", ", length)
            # 같으면 바로 정답 도출
            if word == endWord:
                return length
            # 현재 단어의 모든 글자를 다 하나씩 바꿔보면서 wordList에 있으면 q에 append
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    #print(next_word, word[:i], c, word[i+1:])
                    
                    # 하나씩 바꾼것 중에 wordList에 있는게 걸리면, length +=1해서 append
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
                        #print(wordList, queue)
        return 0