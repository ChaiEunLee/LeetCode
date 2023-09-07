#include <stdio.h>
#include <stdlib.h>


char * convert(char * s, int numRows){
    if (numRows == 1){return s;}
    size_t n = strlen(s);
    char * out = malloc((n+1)*sizeof(char));
    size_t i = 0; // Index being written on out;

    // First row;
    for (size_t j=0; j<n; j += 2*numRows-2){ // rows수만큼 띄어서 한글자씩 붙이는거니까 첫줄을 완성. zigzag니까 2를 곱하는 것.
        out[i++] = s[j];
    }
    
    // Middle rows
    for (size_t row_number=1; row_number<numRows-1; row_number++){
        for (size_t j = row_number; j<n;){
            out[i++] = s[j]; // j 'going down'
            j += 2*(numRows - 1 - row_number);
            // Find the next j 'going up'
            if (j>=n){break;}
            out[i++] = s[j];

            j += 2*row_number; // Find the next j 'going down'
        }
    }

    // Last row
    for (size_t j = numRows - 1; j<n; j+= 2*numRows-2){
        out[i++] = s[j];
    }
    out[i] = 0;
    return out;
}
