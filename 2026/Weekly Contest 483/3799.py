class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans=[]
        for i in range(len(words)):
            for j in range(len(words)):
                for k in range(len(words)):
                    for l in range(len(words)):
                        if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l and words[i][0]==words[j][0] and words[i][-1]==words[k][0] and words[l][0]==words[j][-1] and words[l][-1]==words[k][-1]:
                            ans.append([words[i],words[j],words[k],words[l]])
        return sorted(ans)
