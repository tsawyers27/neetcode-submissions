class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s
            encoded += "~"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        tmp = ""
        for char in s:
            if char != "~":
                tmp += char
            else:
                decoded.append(tmp)
                tmp = ""
                continue
        return decoded
