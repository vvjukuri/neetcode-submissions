class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {
            ")" : "(",
            "]" :"[",
            "}" : "{"
        }
        for character in s:
            if character in pairs:
                if not seen or seen[-1] != pairs[character]:
                    return False
                seen.pop()
            else:
                seen.append(character)
        return len(seen) == 0