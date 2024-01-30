'''2027. Minimum Moves to Convert String
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.

 '''
class Solution:
    def minimumMoves(self, s: str) -> int:
        count=0
        i = 0
        while i<len(s):
            if s[i]=='O':
                i+=1
            else:
                i+=3
                count+=1
        return count