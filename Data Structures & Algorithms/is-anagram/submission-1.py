class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        for letter in s:
            if letter in s_letters.keys():
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1
        for letter in t:
            if letter in t_letters.keys():
                t_letters[letter] += 1
            else:
                t_letters[letter] = 1
        
        if len(s_letters) != len(t_letters):
            return False
        else:
            for key, value in s_letters.items():
                if key not in t_letters.keys():
                    return False
                if t_letters[key] != value:
                    return False
        return True