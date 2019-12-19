class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter

        lsecret = list(secret)
        lguess = list(guess)
        A=0
        for index,gnum in enumerate(lguess):
            if gnum == lsecret[index]:
                A += 1
        B = sum((Counter(secret)&Counter(guess)).values())-A

        return str(A)+'A'+str(B)+'B'
        
