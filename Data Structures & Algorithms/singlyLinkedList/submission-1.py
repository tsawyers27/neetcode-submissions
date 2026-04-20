class LinkedList:
    
    def __init__(self):
        self.ll = list()
    
    def get(self, index: int) -> int:
        if index > len(self.ll) - 1:
            return -1
        else:
            return self.ll[index]

    def insertHead(self, val: int) -> None:
        tmp = []
        tmp.append(val)
        for element in self.ll:
            tmp.append(element)
        self.ll = tmp

    def insertTail(self, val: int) -> None:
        self.ll.append(val)

    def remove(self, index: int) -> bool:
        if index > len(self.ll) - 1:
            return False
        else:
            self.ll.pop(index)
            return True

    def getValues(self) -> List[int]:
        return self.ll
