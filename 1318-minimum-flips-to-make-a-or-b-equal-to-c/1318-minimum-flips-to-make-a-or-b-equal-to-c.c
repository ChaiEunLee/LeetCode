int minFlips(int a, int b, int c){
    int flips = 0; // Counter to track the number of flips required
    for (int i=0; i<32; i++){
        // Extract the i-th bit of a,b and c
        int bitA = (a>>i) & 1;
        int bitB = (b>>i) & 1;
        int bitC = (c>>i) & 1;

        // Check if the i-th bit of (a OR b) is equal to the i-th bit of c
        if ((bitA|bitB) != bitC){
            if (bitC == 1){
                flips++; // Flip required to make the i-th bit of (a OR b) equal to 1
            } else {
                flips += (bitA == 1) + (bitB == 1); // Flips required to make both bits of a and b equal to 0
            }
        }
    }
    return flips;
}