class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "]": "[", "}": "{", ">": "<"}
        keys = map.keys()
        values = map.values()
        for character in s:
            if character in values:
                stack.append(character)
            elif character in keys:
                if stack:
                    if stack.pop() == map[character]:
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True