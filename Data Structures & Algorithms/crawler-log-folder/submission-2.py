class Solution:
    def minOperations(self, logs: List[str]) -> int:
        place = 0

        for com in logs:
            if(com == "../"):
                place += 1
            elif(com == "./"):
                pass
            else:
                print(place)
                place -= 1

        return abs(place)