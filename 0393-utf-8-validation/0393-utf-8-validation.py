class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start+1, start+size+1):
                if i>=len(data) or (data[i]>>6) != 0b10:
                    return False
            return True
        
        start = 0
        while start<len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            # 1 bytes : 0b0xx.., 2 bytes: 0b110x... 이걸 몰랐네!
            first = data[start]
            if (first>>3)==0b11110 and check(3):
                start += 4
            elif (first>>4)==0b1110 and check(2):
                start += 3
            elif (first>>5)==0b110 and check(1):
                start += 2
            elif (first>>7)==0: #1byte = 0b0xx..여야함. 
                start += 1
            else:
                return False
        return True
