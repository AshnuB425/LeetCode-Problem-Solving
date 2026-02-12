class Solution:
    def countPairs(self, words: List[str]) -> int:
        d=dict()
        for i in range(len(words)):
            ans="0"
            for j in range(1,len(words[i])):
                rem=(ord(words[i][j])-ord(words[i][j-1]))%26
                ch=chr(rem+97)
                ans+=ch
            if ans in d:
                d[ans]+=1
            else:
                d[ans]=1
        c=0
        for i,j in d.items():
            c+=(j*(j-1))//2
        return c
