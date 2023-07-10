class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        word = [''] #make as list
        for letter in s:
            if letter.isalpha():
                word = [i+j for i in word for j in [letter.lower(), letter.upper()]]
            else:
                word = [i+letter for i in word]
        return word