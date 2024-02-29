import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        
        # Make original word dict
        ori_word_dict = collections.defaultdict(int) 
        for word in words:
            ori_word_dict[word] += 1
            
        all_word_len = len(words)*word_len
        result = []
        
        # 0,3,6,9 => 1,4,7,9 => 2,5,8,... (word 첫글자 돌고, 두번째글자 돌고 하는 방식)
        for i in range(word_len):
            queue = deque()
            word_dict = ori_word_dict.copy()
            for j in range(i,len(s)-word_len+1, word_len):
                word = s[j:j+word_len]
                # step
                if word_dict.get(word,0) != 0: #get: word 찾고, 없으면 0을 넣는다
                    word_dict[word] -= 1
                    queue.append(word)
                    # 다 된거같으면
                    if sum(word_dict.values())==0:
                        result.append(j-all_word_len+word_len) #index 넣기
                        last_element = queue.popleft() #이제 옆으로 이동하려고 마지막에 넣은 단어 찾고
                        word_dict[last_element] = word_dict.get(last_element,0) + 1 #그거 index+1부터 다시 시작
                else:
                    while len(queue):
                        last_element = queue.popleft()
                        if last_element == word:
                            queue.append(word)
                            break
                        else:
                            word_dict[last_element] = word_dict.get(last_element, 0) + 1
                            if word_dict[last_element] > ori_word_dict[last_element]:
                                word_dict = ori_word_dict.copy()
        return result
                        
            