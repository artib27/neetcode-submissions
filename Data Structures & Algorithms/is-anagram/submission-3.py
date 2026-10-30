class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        if (len(s) != len(t) ) :
            return False
        for letter in s :
            if letter in dict_s:
                dict_s[letter] += 1 
            else :
                 dict_s[letter] = 1       
        for let in t :
            if let in dict_s:
                if dict_s[let]==0:
                    return False
                dict_s[let] -=1 
            else:    
                return False

        if all(v == 0 for v in dict_s.values()):
                return True   
        else:
            return False    