class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict(zip(heights,names))
        names.clear()
        for key in sorted(d.keys(),reverse=True):
            names.append(d[key])
        return names