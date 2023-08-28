bool isPalindrome(char * s){
    int slen = 0;
    while (s[slen]!='\0'){
        slen++;
    }

    int l = 0, r = slen;
    while(l<r){
        while (l<r && !(isalnum(s[l]))){l++;}
        while (l<r && !(isalnum(s[r]))){r--;}
        if (tolower(s[l])!=tolower(s[r])){
            return false;
        }
        l++; r--;
    }
    return true;
}