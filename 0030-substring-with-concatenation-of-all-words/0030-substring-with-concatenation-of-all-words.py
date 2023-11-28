from collections import deque, defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        ori_word_dict = defaultdict(int) # 디폴트 값이 int인 딕셔너리
        
        for word in words:
            ori_word_dict[word] += 1 # 이미 dict에 있는지 없는지 체크 안해도 되고 += 1 해주면 됨..!
            
        all_word_len = len(words) * word_len #s의 최소 길이
        result = []
        
        for i in range(word_len):
            queue = deque()
            word_dict = ori_word_dict.copy()
            for j in range(i, len(s) - word_len + 1, word_len): # 시작지점 달리하면서 +word_len 만큼씩 띄어가며 읽기
                word = s[j:j + word_len]
                if word_dict.get(word, 0) != 0: #word가 없으면 0을 반환해주는데 != 0 : 그 단어가 있다면
                    word_dict[word] -= 1 #-1해주고
                    queue.append(word) #word가 있으면 queue에 넣어줌
                    if sum(word_dict.values()) == 0: #word_dict에서 단어 다 빼면
                        result.append(j - all_word_len + word_len)
                        last_element = queue.popleft()
                        word_dict[last_element] = word_dict.get(last_element, 0) + 1
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
        