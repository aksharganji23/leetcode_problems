class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = set("qwertyuiop")
        l2 = set("asdfghjkl")
        l3 = set("zxcvbnm")
        ans = []
        for i in words:
            lower_word = set(i.lower())
            if lower_word <= l1 or lower_word <= l2 or lower_word <= l3:
                ans.append(i)
        return ans
