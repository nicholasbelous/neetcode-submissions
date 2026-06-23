class LinkedList:
    
    def __init__(self):
        self.list = []
    
    def get(self, index: int) -> int:
        if(index >= len(self.list)):
            return -1
        return self.list[index]

    def insertHead(self, val: int) -> None:
        self.list.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.list.append(val)

    def remove(self, index: int) -> bool:
        if(index >= len(self.list)):
            return False
        self.list.pop(index)
        return True

    def getValues(self) -> List[int]:
        return self.list
