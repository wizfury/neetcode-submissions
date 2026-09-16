class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            key = ''.join(sorted(st))
            if key not in res:
                res[key]=[st]
            else:
                res[key].append(st)
        return list(res.values())
        