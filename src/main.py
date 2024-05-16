from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    # win.draw_line(Line(Point(0, 0), Point(250, 250)), "black")
    cell = Cell(win)
    cell.has_right_wall = False
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)
    win.wait_for_close()
    

main()