import pyautogui as gui

MOVE = "MOVE"
SCROLL = "SCROLL"


class Rat:
    def __init__(self):
        self.width, self.height = gui.size()
        self.step = 100
        self.step_scalling = 5
        self.scroll_step = 10
        self.mode = MOVE
        self.mouse_down = False

    def move_to(self, x, y):
        if x is not None:
            x = max(1, min(self.width - 2, x))
        if y is not None:
            y = max(1, min(self.height - 2, y))
        gui.moveTo(x, y)

    def mid_y(self):
        self.move_to(None, self.height / 2)

    def mid_x(self):
        self.move_to(self.width / 2, None)

    def step_up(self):
        max_step = self.height / 3
        self.step = min(max_step, self.step * self.step_scalling)
        self.scroll_step = max(1, self.step / 10)

    def step_down(self):
        min_step = 3
        self.step = max(min_step, self.step / self.step_scalling)
        self.scroll_step = max(1, self.step / 10)

    def click(self):
        gui.click()

    def half_click(self):
        if self.mouse_down:
            gui.mouseUp()
        else:
            gui.mouseDown()
        self.mouse_down = not self.mouse_down

    def toggle_mode(self):
        if self.mode == MOVE:
            self.mode = SCROLL
        else:
            self.mode = MOVE

    def down(self):
        if self.mode == MOVE:
            _, y = gui.position()
            self.move_to(None, y + self.step)
        if self.mode == SCROLL:
            gui.vscroll(-self.scroll_step)

    def up(self):
        if self.mode == MOVE:
            _, y = gui.position()
            self.move_to(None, y - self.step)
        if self.mode == SCROLL:
            gui.vscroll(self.scroll_step)

    def left(self):
        if self.mode == MOVE:
            x, _ = gui.position()
            self.move_to(x - self.step, None)
        if self.mode == SCROLL:
            gui.hscroll(-self.scroll_step)

    def right(self):
        if self.mode == MOVE:
            x, _ = gui.position()
            self.move_to(x + self.step, None)
        if self.mode == SCROLL:
            gui.hscroll(self.scroll_step)

    def all_down(self):
        if self.mode == MOVE:
            self.move_to(None, self.height)
        if self.mode == SCROLL:
            gui.vscroll(-self.scroll_step * 10)

    def all_up(self):
        if self.mode == MOVE:
            self.move_to(None, 0)
        if self.mode == SCROLL:
            gui.vscroll(self.scroll_step * 10)

    def all_left(self):
        if self.mode == MOVE:
            self.move_to(0, None)
        if self.mode == SCROLL:
            gui.hscroll(-self.scroll_step * 10)

    def all_right(self):
        if self.mode == MOVE:
            self.move_to(self.width, None)
        if self.mode == SCROLL:
            gui.hscroll(self.scroll_step * 10)


rat = Rat()
