class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for str in strs:
            for let in str:
                final_string += let
            final_string += "zax420"
        return final_string

    def decode(self, s: str) -> List[str]:
        fin_list = s.split("zax420")
        fin_list.pop()
        
        return fin_list
        
