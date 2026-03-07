class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in map_st and map_st[c1] != c2:
                return False
            if c2 in map_ts and map_ts[c2] != c1:
                return False
            map_st[c1] = c2
            map_ts[c2] = c1
        return True