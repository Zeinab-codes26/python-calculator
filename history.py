import json
class History:
    def __init__(self) -> None:
        self.history_list:list[str]=[]

    def add(self,entry:str) -> None:
        self.history_list.append(str(entry))

    def show(self)-> list[str]:
       return self.history_list.copy()

    def clear(self) -> None:
        self.history_list.clear()

    def save_file(self , filename:str) ->None:
        with open(filename,"w",encoding="utf-8") as f :
            json.dump(self.history_list,f,ensure_ascii=False,indent=4)
    def load_file(self,filename:str) ->None:
        with open (filename,"r",encoding="utf-8")as f:
            data=json.load(f)
            if not isinstance(data,list):
                raise ValueError("Invalid history file format")
            self.history_list=[str(item)for item in data]
