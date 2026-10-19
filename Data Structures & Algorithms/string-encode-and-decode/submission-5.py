class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == None:
            return None
        return "*$*".join(strs)

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        if s == "":
            return [""]
        return s.split("*$*")
