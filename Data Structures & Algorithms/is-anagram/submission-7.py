class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!= len(t)):
            return False
        counter_s,counter_t = {},{}
        for c in s:
            if c in counter_s:
                counter_s[c] +=1
            else:
                counter_s[c] =1
        for c in t:
            if c in counter_t:
                counter_t[c] +=1
            else:
                counter_t[c] =1
        for c in s:
            if counter_s.get(c,0) != counter_t.get(c,0):
                return False
        return True



        