class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if len(guess) == 1:
            if guess == secret:
                return "1A0B"
            else:
                return "0A0B"
        secret = list(secret)
        guess = list(guess)
        A,B=0,0
        for i in range (len(guess)):
            if guess[i] == secret[i]:
                A += 1
                secret[i] = 'X'
                guess[i] = 'X'
        for i in range (len(guess)):
            if guess[i] != 'X':
                if guess[i] in secret:
                    B += 1
                    secret[secret.index(guess[i])] = 'X'
        return str(A)+'A'+str(B)+'B'
        
