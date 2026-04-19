class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        countRes = []
        for s in strs:
            count = {}
            for c in s:
                count[c] = 1 + count.get(c, 0)

            added = False
            for i in range(len(countRes)):
                if countRes[i] == count:
                    res[i].append(s)
                    added = True
                    break
            if not added:
                countRes.append(count)
                res.append([s])
        return res