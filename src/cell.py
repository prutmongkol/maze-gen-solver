from graphics import Point, Line, Window


class Cell():
    def __init__(self, window=None) -> None:
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
        
    def draw(self, x1, y1, x2, y2) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "beige")
        
        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "beige")

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "beige")
        
        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "beige")
    
    def draw_move(self, to_cell, undo=False) -> None:
        start_point = Point(
            (self._x1 + self._x2) // 2,
            (self._y1 + self._y2) // 2
        )
        end_point = Point(
            (to_cell._x1 + to_cell._x2) // 2,
            (to_cell._y1 + to_cell._y2) // 2
        )
        line = Line(start_point, end_point)
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)
