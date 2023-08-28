void reverseString(char* s, int sSize){
    int l = 0, r = sSize-1;
    char tmp;
    while (l<r){
        tmp = s[l];
        s[l] = s[r];
        s[r] = tmp;
        l++; r--;
    }

}

