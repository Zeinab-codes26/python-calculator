class Memory:

    def __init__(self) -> None:
        self.memory_value:float=0.0

    def save(self,value:float) -> None:
        self.memory_value=float(value)

    def  recall(self) ->float:
        return self.memory_value

    def clear(self) -> None:
        self.memory_value=0.0

    def add_memory(self,value:float) ->None:
        self.memory_value+=float(value)

    def subtract_memory(self,value:float)-> None:
        self.memory_value-=float(value)