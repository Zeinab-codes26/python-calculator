import tkinter as tk
from operation import Operation
class GUI:
    def __init__(self,calculator) ->None:
        self.calculator=calculator
        self.window=None
        self.display_var=None
        self.display=None
        self.buttons=[]

    def create_window(self) ->None:
        self.window=tk.Tk()
        self.window.title("Professional Calculator")
        self.window.geometry("360x520")
        self.window.resizable(False,False)

    def create_display(self)->None:
        self.display_var=tk.StringVar(value="")
        self.display=tk.Entry(
            self.window,
            textvariable=self.display_var,
            font=("Arial",24),
            justify="right",
            bd=10,
            relief="sunken"
        )
        self.display.pack(fill="x",padx=10,pady=10,ipady=10)

    def create_buttons(self)->None:
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both",padx=10,pady=10)
        button_texts=["/","%","C","DEL",
                      "*","9","8","7",
                      "-","6","5","4",
                      "+","3","2","1",
                      "M+","=",".","0"
                                      ]
        rows=5
        cols=4
        for i in range(rows):
            frame.rowconfigure(i,weight=1)
        for j in range(cols):
            frame.columnconfigure(j,weight=1)

        for index , text in enumerate(button_texts):
            row=index// cols
            col=index% cols
            btn=tk.Button(
                frame,
                text=text,
                font=("Arial",18),
                command=lambda t=text:
            self.button_clicked(t))
            btn.grid(row=row,column=col,sticky="nsew",padx=4,pady=4)
            self.buttons.append(btn)

    def button_clicked(self,value:str) -> None:
        if value =="C":
            self.calculator.clear()
        elif value=="DEL":
            self.calculator.delete_last()
        elif value =="=":
            self.calculator.calculate(self.calculator.current_expression)
        elif value=="M+":
            result=self.calculator.get_result()
            if isinstance(result,(int,float)):
                self.calculator.memory.add_memory(result)
        elif value=="%":
            self.calculator.append_character("/100")
        else:
            self.calculator.append_character(value)
        self.update_display()

    def update_display(self) -> None:
        result=self.calculator.get_result()
        if result is not None:
            self.display_var.set(str(result))
        else:
            self.display_var.set(self.calculator.current_expression)

    def run(self) -> None:

        self.create_window()
        self.create_display()
        self.create_buttons()
        self.update_display()
        self.window.mainloop()


