from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Gen & Solver"
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self) -> None:
        self.__running = False
        