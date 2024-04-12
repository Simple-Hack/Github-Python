import tkinter as tk

ALGORITHMS = {
    'BFS': generatePath_BFS,
    'Dijkstra': generatePath_Dijkstra,
    'A*': generatePath_AStar,
}

class MiniMap:
    def __init__(self, *args):
        # ... （现有初始化代码）

        self.start = None
        self.end = None
        self.obstacles = set()
        self.selected_algorithm = None
        self.current_mode = 'SELECT_START_END'

        self.canvas.bind('<Button-1>', self.handle_click)
        self.root.bind('<Key>', self.handle_key)

        self.algorithm_menu = tk.Menu(self.root, tearoff=0)
        for alg_name in ALGORITHMS.keys():
            self.algorithm_menu.add_radiobutton(label=alg_name, variable=self.selected_algorithm, value=alg_name)
        self.root.bind('<F1>', lambda _: self.algorithm_menu.post(event.x_root, event.y_root))

        self.root.mainloop()

    def handle_click(self, event):
        x, y = self.get_canvas_cell(event.x, event.y)
        if not (0 <= x < self.width and 0 <= y < self.height):
            return  # 点击位置不在地图范围内，忽略

        cell_state = self.grid[y][x]

        if self.current_mode == 'SELECT_START_END':
            if self.start is None:
                self.start = (x, y)
                self.draw_start(x, y)
            elif self.end is None:
                self.end = (x, y)
                self.draw_end(x, y)
                self.switch_to_next_mode()
        elif self.current_mode == 'PLACE_OBSTACLES':
            if cell_state == UNUSED:
                self.grid[y][x] = BARRIER
                self.draw_barrier(x, y)
            else:
                self.grid[y][x] = UNUSED
                self.draw_unused(x, y)
        # ... （其他模式的处理）

    def switch_to_next_mode(self):
        if self.current_mode == 'SELECT_START_END':
            self.current_mode = 'PLACE_OBSTACLES'
            self.clear_selections()
            self.canvas.delete('obstacle')
            self.canvas.delete('path')
            self.draw_grid()  # 重新绘制地图，显示起点和终点
        elif self.current_mode == 'PLACE_OBSTACLES':
            self.current_mode = 'CHOOSE_ALGORITHM'
            self.clear_selections()
            self.canvas.delete('obstacle')
            self.canvas.delete('path')
            self.draw_grid()  # 重新绘制地图，显示起点、终点和障碍物
        elif self.current_mode == 'CHOOSE_ALGORITHM':
            if self.selected_algorithm is not None:
                path = ALGORITHMS[self.selected_algorithm](self.grid, self.start, self.end)
                self.draw_path(path)
                self.current_mode = 'PATH_SHOWN'
            else:
                self.root.bell()  # 提示用户未选择算法

    def handle_key(self, event):
        # ... （键盘事件处理，用于切换模式等操作）

    def get_canvas_cell(self, canvas_x, canvas_y):
        # ... （将屏幕坐标转换为地图单元格坐标）

    def draw_start(self, x, y):
        # ... （在画布上绘制起点标记）

    def draw_end(self, x, y):
        # ... （在画布上绘制终点标记）

    def draw_barrier(self, x, y):
        # ... （在画布上绘制障碍物标记）

    def draw_unused(self, x, y):
        # ... （在画布上绘制未使用的单元格）

    def clear_selections(self):
        # ... （清除已选中的起点和终点标记）

    def draw_grid(self):
        # ... （绘制整个地图，包括已有的起点、终点和障碍物）

    def draw_path(self, path):
        # ... （绘制计算出的路径）

    def generatePath_BFS(self, grid, start, end):
        # ... （广度优先搜索算法实现）

    def generatePath_Dijkstra(self, grid, start, end):
        # ... （Dijkstra算法实现）

    def generatePath_AStar(self, grid, start, end):
        # ... （A*算法实现）