from history import History
from operation import Operation
from memory import Memory

class Calculator:
    def __init__(self) ->None:

        self.memory= Memory()
        self.history=History()
        self.current_expression:str=""
        self.result:float|None=None

    def calculate(self,expression:str) -> None:
        self.current_expression=expression
        return self.evaluate()

    def clear(self) ->None:
        self.current_expression=""
        self.result=None

    def delete_last(self) ->None:
        self.current_expression=self.current_expression[:-1]

    def evaluate(self) ->None:
        try:
            self.result=eval(self.current_expression,{"__builtins__":{}},{})
            self.history.add(f"{self.current_expression}={self.result}")
            return self.result
        except Exception :
            self.result="Error"
            return self.result


    def save_history(self,filename:str) -> None:
        self.history.save_file(filename)


    def append_character(self,char:str) ->None:
        self.current_expression+=char

    def get_result(self):
        return self.result

