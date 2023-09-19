int strStr(char * haystack, char * needle){
    char *occurence = strstr(haystack, needle);
    if (occurence) return occurence - haystack;
    else return -1;
}