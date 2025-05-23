"""
# Time: O(n) — Where n is the length of the strings s and t (which are same).
# Space: O(k) - hence O(1) — where k is the number of unique characters (at most 52 for alphabets).
# Did this code successfully run on Leetcode : Yes.
# Any problem you faced while coding this : No
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Two Hasmap solution
        if len(s)!= len(t):
            return False

        smap = {}
        tmap = {}

        for i in range(len(s)):
            if smap.get(s[i]):
                if smap[s[i]] != t[i]:
                    return False
            else: 
                smap[s[i]] = t[i]
            
            if tmap.get(t[i]):
                if tmap[t[i]] != s[i]:
                    return False
            else:
                tmap[t[i]] = s[i]

        return True


        #One HashMap + One Set solution
        if len(s)!= len(t):
            return False

        smap = {}
        tset = set()

        for i in range(len(s)):
            if smap.get(s[i]):
                if smap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in tset:
                    return False
                smap[s[i]] = t[i]
                tset.add(t[i])

        return True


        #Two array problem:
        if len(s)!=len(t):
            return False

        sarr = 128*[-1]
        tarr = 128*[-1]

        for i in range(len(s)):
            sch = ord(s[i])
            tch = ord(t[i])

            if sarr[sch]!=-1:
                if sarr[sch]!=tch:
                    return False
            else:
                sarr[sch]=tch
            
            if tarr[tch]!=-1:
                if tarr[tch]!=sch:
                    return False
            else:
                tarr[tch]=sch
            
        return True