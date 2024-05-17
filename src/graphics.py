from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1: Point, p2: Point) -> None:
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas: Canvas, fill_color="black") -> None:
        canvas.create_line(
            self.__p1.x, self.__p1.y,
            self.__p2.x, self.__p2.y,
            fill=fill_color,
            width=2
        )
        

class Window():
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Gen & Solver"
        self.__canvas = Canvas(self.__root, background="beige", height=height, width=width)
        self.__canvas.pack(expand=1, fill=BOTH)
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
        
    def draw_line(self, line: Line, fill_color="black") -> None:
        line.draw(self.__canvas, fill_color)
