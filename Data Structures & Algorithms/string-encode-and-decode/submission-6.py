class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "Error"
        return "*$*".join(strs)

    def decode(self, s: str) -> List[str]:
        if s is "Error":
            return []
        if s == "":
            return [""]
        return s.split("*$*")
