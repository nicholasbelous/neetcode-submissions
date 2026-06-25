class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for str in strs:
            for let in str:
                final_string += let
            final_string += "xyz"
        return final_string

    def decode(self, s: str) -> List[str]:
        fin_list = s.split("xyz")
        fin_list.pop()
        
        return fin_list
        
