import pyautogui as gui
from libqtile.config import Key, KeyChord
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from libqtile.widget import TextBox

WIDTH, HEIGHT = gui.size()
MIN_X, MAX_X = 1, WIDTH - 2
MIN_Y, MAX_Y = 1, HEIGHT - 2

MIN_SPEED, MAX_SPEED = 3, max(WIDTH / 3, HEIGHT / 3)

MOD, ALT, CTRL, SHIFT = "mod4", "mod1", "control", "shift"
SPACE, RETURN, DOT, COMMA = "space", "return", "period", "comma"
J, K, L, H = "j", "k", "l", "h"

LEFT, MIDDLE, RIGHT = "left", "middle", "right"
DECEL, SLIDE, ACCEL = "DECEL", "SLIDE", "ACCEL"


@lazy.function
def cmd(qtile, f, *args, **kwargs):
    f(*args, **kwargs)


class Rat:
    def __init__(self, acceleration=1.2, deceleration=0.8):
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.mode = SLIDE
        self.button = LEFT
        self.scroll = False
        self.down = False
        self.memory = None
        self.widget = TextBox("")
        self.key = KeyChord(
            [MOD],
            "r",
            [Key([], key, cmd(self.step, key)) for key in [J, K, L, H]]
            + [Key([SHIFT], key, cmd(self.jump, key)) for key in [J, K, L, H]]
            + [
                Key(
                    [], "a", cmd(self.set_mode, SLIDE), cmd(self.accel), cmd(self.step)
                ),
                Key([], "s", cmd(self.set_mode, SLIDE), cmd(self.step)),
                Key(
                    [], "d", cmd(self.set_mode, SLIDE), cmd(self.decel), cmd(self.step)
                ),
                Key([SHIFT], "a", cmd(self.set_mode, ACCEL)),
                Key([SHIFT], "s", cmd(self.set_mode, SLIDE)),
                Key([SHIFT], "d", cmd(self.set_mode, DECEL)),
                Key([], "f", cmd(self.toggle_scroll)),
                Key([], "u", cmd(self.undo)),
                Key([], RETURN, cmd(self.click)),
                Key([SHIFT], RETURN, cmd(self.half_click)),
                Key([], "r", cmd(self.click, RIGHT)),
                Key([SHIFT], "r", cmd(self.half_click, RIGHT)),
            ],
            cmd(self.reset),
            escape_command=cmd(self.exit),
            mode=True,
            name="RAT",
        )

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
        self.clicks = max(1, value // 25)

    def reset(self):
        self.scroll = False
        self.speed = MIN_SPEED ** (2 * self.acceleration)
        self.render()

    def exit(self):
        self.widget.update("")

    def render(self):
        char = "_" if self.down else "-"
        speed = char * max(int(self.speed ** (0.75 / self.acceleration)), 1)
        icons = []
        if self.scroll:
            icons.append("📜")
        if self.mode == DECEL:
            icons.append("🐌")
        if self.mode == ACCEL:
            icons.append("🚀")
        mode = " ".join(icons)
        self.widget.update(" ".join([f"|{speed}|", mode, "🐀"]))

    def toggle_scroll(self):
        self.scroll = not self.scroll
        self.button = MIDDLE if self.scroll else LEFT

    def set_mode(self, mode):
        self.mode = mode if self.mode != mode else SLIDE
        self.render()

    def click(self, button=None):
        button = button if button else self.button
        if self.down:
            gui.mouseUp(button=button)
            self.down = False
        else:
            gui.click(button=button)
        self.reset()

    def half_click(self, button=LEFT):
        if self.down:
            gui.mouseUp(button=button)
        else:
            gui.mouseDown(button=button)
        self.down = not self.down
        self.reset()

    def move_to(self, x, y):
        x = max(min(x, MAX_X), MIN_X) if x is not None else None
        y = max(min(y, MAX_Y), MIN_Y) if y is not None else None
        gui.moveTo(x, y)

    def step(self, key=None):
        if self.mode == ACCEL:
            self.accel()
        if self.mode == DECEL:
            self.decel()
        key = key if key is not None else self.memory
        self.memory = key
        if self.scroll:
            scroll, clicks = {
                J: (gui.vscroll, -self.clicks),
                K: (gui.vscroll, +self.clicks),
                L: (gui.hscroll, +self.clicks),
                H: (gui.hscroll, -self.clicks),
            }[key]
            scroll(clicks)
            return
        dx, dy = {
            J: (None, +self.speed),
            K: (None, -self.speed),
            L: (+self.speed, None),
            H: (-self.speed, None),
        }[key]
        x, y = gui.position()
        x = x + dx if dx is not None else None
        y = y + dy if dy is not None else None
        self.move_to(x, y)

    def undo(self):
        key = {
            J: K,
            K: J,
            L: H,
            H: L,
        }[self.memory]
        self.step(key)

    def jump(self, key):
        x, y = {
            J: (None, HEIGHT),
            K: (None, 0),
            L: (WIDTH, None),
            H: (0, None),
        }[key]
        logger.warning(f"JUMP {x=}, {y=}")
        self.move_to(x, y)

    def accel(self):
        self.speed = min(self.speed**self.acceleration, MAX_SPEED)
        self.render()

    def decel(self):
        self.speed = max(self.speed**self.deceleration, MIN_SPEED)
        self.render()
