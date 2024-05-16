from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(250, 250)), "black")
    win.wait_for_close()
    

main()