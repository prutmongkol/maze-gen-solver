import time
from cell import Cell
from graphics import Window


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window: Window,
        ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self._cells = None
        self._create_cells()
    
    def _create_cells(self) -> None:
        self._cells = [
            [
                Cell(self._win) for j in range(self._num_cols)
            ] for i in range(self._num_rows)
        ]
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j) -> None:
        if self._win is None:
            return
        col_offset = j * self._cell_size_x
        row_offset = i * self._cell_size_y
        x1 = self._x1 + col_offset
        y1 = self._y1 + row_offset
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        