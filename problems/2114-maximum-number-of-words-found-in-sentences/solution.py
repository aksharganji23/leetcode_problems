class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=[]
        for i in range(len(sentences)):
            words=sentences[i].split()
            count.append(len(words))
        return max(count)
