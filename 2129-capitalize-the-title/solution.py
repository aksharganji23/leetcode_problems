class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res=title.lower().split()
        s=[]
        for i in res:
            if len(i)>2:
                s.append(i.capitalize())
            else:
                s.append(i)
        final=" ".join(s)
        return final 