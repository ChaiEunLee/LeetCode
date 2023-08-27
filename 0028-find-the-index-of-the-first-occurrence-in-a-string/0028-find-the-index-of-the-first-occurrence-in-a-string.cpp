class Solution {
public:
    int strStr(string haystack, string needle) {
        // string::size()는 unsigned int라서 그걸 그대로 쓰면 m=0 일때 m-n<0이 돼서 error
        // 그래서 int m = haystack.size()로 정의해서 써야 오류 안 남.
        int m = haystack.size(), n = needle.size();
        for (int i=0; i<= m-n; i++){
            int j = 0;
            for (; j < n; j++){ // j가 이미 위에서 정의됐으니까 초기화 할 필요 없음
                if (haystack[i+j] != needle[j]){
                    break;
                }
            }
            if (j==n){return i;}
        }
        return -1;
    }
};