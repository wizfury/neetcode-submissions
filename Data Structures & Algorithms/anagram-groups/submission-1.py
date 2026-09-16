class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            key=[0]*26
            for s in st:
                key[ord(s)-ord('a')]+=1
           
            key=tuple(key)
           
            if key not in res:
                res[key] = [st]
            else:
                res[key].append(st) 
        return list(res.values())
        