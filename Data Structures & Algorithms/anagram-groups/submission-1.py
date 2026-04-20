class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                    "m": 0,"n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
                        "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,"z": 0}
            for letter in s:
                alphabet[letter] += 1
            char_count = tuple(alphabet.items())
            if char_count not in map.keys() or len(map.keys()) == 0:
                map[char_count] = [s]
            elif char_count in map.keys():
                map[char_count].append(s)
        result = list(map.values())
        return result