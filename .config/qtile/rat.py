import pyautogui as gui
from libqtile.lazy import lazy

MOVE = "MOVE"
SCROLL = "SCROLL"
DRAG = "DRAG"


class Rat:
    def __init__(self):
        self.width, self.height = gui.size()
        self.step = 100
        self.step_scalling = 5
        self.click = 10
        self.mode = MOVE
        self.mouse_down = False

    def clip(self, x, y):
        if x is not None:
            x = max(1, min(self.width - 2, x))
        if y is not None:
            y = max(1, min(self.height - 2, y))
        return x, y

    def move_to(self, x, y):
        x, y = self.clip(x, y)
        gui.moveTo(x, y)

    def move_left(self):
        x, _ = gui.position()
        self.move_to(x - self.step, None)

    def move_right(self):
        x, _ = gui.position()
        self.move_to(x + self.step, None)

    def move_up(self):
        _, y = gui.position()
        self.move_to(None, y - self.step)

    def move_down(self):
        _, y = gui.position()
        self.move_to(None, y + self.step)

    def move_all_left(self):
        self.move_to(0, None)

    def move_all_right(self):
        self.move_to(self.width, None)

    def move_all_up(self):
        self.move_to(None, 0)

    def move_all_down(self):
        self.move_to(None, self.height)

    def drag_to(self, x, y):
        x, y = self.clip(x, y)
        gui.dragTo(x, y, button="left")

    def drag_left(self):
        x, _ = gui.position()
        self.drag_to(x - self.step, None)

    def drag_right(self):
        x, _ = gui.position()
        self.drag_to(x + self.step, None)

    def drag_up(self):
        _, y = gui.position()
        self.drag_to(None, y - self.step)

    def drag_down(self):
        _, y = gui.position()
        self.drag_to(None, y + self.step)

    def drag_all_left(self):
        self.drag_to(0, None)

    def drag_all_right(self):
        self.drag_to(self.width, None)

    def drag_all_up(self):
        self.drag_to(None, 0)

    def drag_all_down(self):
        self.drag_to(None, self.height)

    def scroll_left(self):
        gui.hscroll(-self.click)

    def scroll_right(self):
        gui.hscroll(self.click)

    def scroll_up(self):
        gui.vscroll(self.click)

    def scroll_down(self):
        gui.vscroll(-self.click)

    def scroll_all_left(self):
        gui.hscroll(-self.click * 10)

    def scroll_all_right(self):
        gui.hscroll(self.click * 10)

    def scroll_all_up(self):
        gui.vscroll(self.click * 10)

    def scroll_all_down(self):
        gui.vscroll(-self.click * 10)

    def step_up(self):
        max_step = self.height / 3
        self.step = min(max_step, self.step * self.step_scalling)
        self.click = max(1, self.step / 10)

    def step_down(self):
        min_step = 3
        self.step = max(min_step, self.step / self.step_scalling)
        self.click = max(1, self.step / 10)

    def mouse_click(self):
        gui.click()

    def mouse_half_click(self):
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
            self.move_down()
        if self.mode == SCROLL:
            self.scroll_down()

    def up(self):
        if self.mode == MOVE:
            self.move_up()
        if self.mode == SCROLL:
            self.scroll_up()

    def left(self):
        if self.mode == MOVE:
            self.move_left()
        if self.mode == SCROLL:
            self.scroll_left()

    def right(self):
        if self.mode == MOVE:
            self.move_right()
        if self.mode == SCROLL:
            self.scroll_right()

    def all_down(self):
        if self.mode == MOVE:
            self.move_all_down()
        if self.mode == SCROLL:
            self.scroll_all_down()

    def all_up(self):
        if self.mode == MOVE:
            self.move_all_up()
        if self.mode == SCROLL:
            self.scroll_all_up()

    def all_left(self):
        if self.mode == MOVE:
            self.move_all_left()
        if self.mode == SCROLL:
            self.scroll_all_left()

    def all_right(self):
        if self.mode == MOVE:
            self.move_all_right()
        if self.mode == SCROLL:
            self.scroll_all_right()


rat = Rat()


@lazy.function
def step_up(qtile):
    rat.step_up()


@lazy.function
def step_down(qtile):
    rat.step_down()


@lazy.function
def toggle_mode(qtile):
    rat.toggle_mode()


@lazy.function
def down(qtile):
    if rat.mode == MOVE:
        rat.move_down()
    if rat.mode == SCROLL:
        rat.scroll_down()
    if rat.mode == DRAG:
        rat.drag_down()


@lazy.function
def up(qtile):
    if rat.mode == MOVE:
        rat.move_up()
    if rat.mode == SCROLL:
        rat.scroll_up()
    if rat.mode == DRAG:
        rat.drag_up()


@lazy.function
def left(qtile):
    if rat.mode == MOVE:
        rat.move_left()
    if rat.mode == SCROLL:
        rat.scroll_left()
    if rat.mode == DRAG:
        rat.drag_left()


@lazy.function
def right(qtile):
    if rat.mode == MOVE:
        rat.move_right()
    if rat.mode == SCROLL:
        rat.scroll_right()
    if rat.mode == DRAG:
        rat.drag_right()


@lazy.function
def all_down(qtile):
    if rat.mode == MOVE:
        rat.move_all_down()
    if rat.mode == SCROLL:
        rat.scroll_all_down()


@lazy.function
def all_up(qtile):
    if rat.mode == MOVE:
        rat.move_all_up()
    if rat.mode == SCROLL:
        rat.scroll_all_up()


@lazy.function
def all_left(qtile):
    if rat.mode == MOVE:
        rat.move_all_left()
    if rat.mode == SCROLL:
        rat.scroll_all_left()


@lazy.function
def all_right(qtile):
    if rat.mode == MOVE:
        rat.move_all_right()
    if rat.mode == SCROLL:
        rat.scroll_all_right()


@lazy.function
def click(qtile):
    rat.mouse_click()


@lazy.function
def half_click(qtile):
    rat.mouse_half_click()
