class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = len(sentences[0].split(" "))
        
        for i in range(1,len(sentences)):
            if len(sentences[i].split(" ")) > res: 
                res = len(sentences[i].split(" "))
                print(res)
        return res