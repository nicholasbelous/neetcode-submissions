class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if(len(num) < 3):
            return ""

        curMax = -1
        curNum = num[0:3]
        returnVal = ""


        for n in range(3 , len(num)):
            curNum = curNum[1:3] + num[n]
            if(int(curNum) > curMax):
                if(curNum[0] == curNum[1] and curNum[1] == curNum[2]):
                    curMax = int(curNum)
                    returnVal = curNum
        if(curMax == -1):
            return ""

        if(curMax == 0):
            return "000"

        return str(curMax)