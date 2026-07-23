from calculator import Calculator
from gui import GUI

def main():

    calculator=Calculator()

    gui=GUI(calculator)

    gui.run()

if __name__=="__main__":
    main()