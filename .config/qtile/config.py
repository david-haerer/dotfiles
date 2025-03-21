import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile.widget import base


def run(cmd):
    try:
        return subprocess.run(cmd, text=True, capture_output=True).stdout.strip()
    except FileNotFoundError:
        return "-"


class VPN(base.InLoopPollText):
    def poll(self):
        status = run(["mullvad", "status"]).split("\n")[0]
        return f"VPN: {status}"


# -- CONSTANTS --

MOD = "mod4"
ALT = "mod1"
ALTGR = "mod5"
HASHTAG = "numbersign"
CTRL = "control"
SHIFT = "shift"
SUPER = "Super_L"

AUDIO_MUTE = "XF86AudioMute"
AUDIO_DOWN = "XF86AudioLowerVolume"
AUDIO_UP = "XF86AudioRaiseVolume"
BRIGHTNESS_DOWN = "XF86MonBrightnessUp"
BRIGHTNESS_UP = "XF86MonBrightnessDown"

USER = os.getenv("USER")
FONT = os.getenv("FONT")
TERMINAL = os.getenv("TERMINAL", "wezterm")
SIGNAL = "signal-desktop"
BROWSER = os.getenv("BROWSER", "firefox")
LAUNCHER = "rofi -display-drun 'Launch' -show drun"
PASSWORD_MANAGER = "passmenu"

BLACK = "#0A0E14"
GRAY = "#4D5566"
WHITE = "#B3B1AD"
RED = "#FF3333"
ORANGE = "#E6B450"
YELLOW = "#FF8F40"
GREEN = "#C2D94C"
CYAN = "#95E6CB"
BLUE = "#59C2FF"
MAGENTA = "#FFEE99"

ACCENT_COLOR = YELLOW
BACKGROUND = BLACK
FOREGROUND = WHITE


@hook.subscribe.layout_change
def layout_change(layout, group):
    value = 1 if layout.name == "max" else 0
    for window in group.windows:
        window_value = 0 if window.floating else value
        window.window.set_property("QTILE_MAX", window_value, "CARDINAL", 32)


@hook.subscribe.group_window_add
def group_window_add(group, window):
    value = 1 if group.layout.name == "max" and not window.floating else 0
    window.window.set_property("QTILE_MAX", value, "CARDINAL", 32)


@hook.subscribe.client_focus
def client_focus(client):
    client.group.set_label(client.name[:25])


@hook.subscribe.client_name_updated
def client_name_updated(client):
    client.group.set_label(client.name[:25])


# -- KEYS --


@lazy.function
def new_group(qtile):
    qtile.add_group(str(len(qtile.groups)), label="New Tab")


@lazy.function
def delete_group(qtile):
    logger.warning("delete_group")
    logger.warning(qtile.current_group)
    if qtile.current_group.windows:
        logger.info(
            f"{qtile.current_group} has windows {qtile.current_group.windows}, not closing"
        )
        return
    qtile.delete_group(qtile.current_group.name)


@lazy.function
def to_next_group(qtile):
    if qtile.current_window is None:
        return
    next_group_index = (
        qtile.groups.index(qtile.current_group) + 1
        if qtile.current_group.name != qtile.groups[-1].name
        else 0
    )
    qtile.current_window.togroup(qtile.groups[next_group_index].name)
    qtile.current_screen.next_group()


@lazy.function
def to_prev_group(qtile):
    logger.warning("to_prev_group")
    if qtile.current_window is None:
        return
    group_index_prev = (
        qtile.groups.index(qtile.current_group) - 1
        if qtile.current_group.name != qtile.groups[0].name
        else -1
    )
    qtile.current_window.togroup(qtile.groups[group_index_prev].name)
    qtile.current_screen.next_group()


@hook.subscribe.selection_notify
def selection_notify(qtile, selection):
    qtile.primary_selection = selection


keys = [
    # Device
    Key([], AUDIO_MUTE, lazy.spawn("amixer -D pulse set Master toggle")),
    Key([], AUDIO_DOWN, lazy.spawn("amixer -D pulse sset Master 7%- unmute")),
    Key([], AUDIO_UP, lazy.spawn("amixer -D pulse sset Master 7%+ unmute")),
    Key([], BRIGHTNESS_UP, lazy.spawn("brightnessctl set 5%+")),
    Key([], BRIGHTNESS_DOWN, lazy.spawn("brightnessctl set 5%-")),
    # Window
    Key([MOD], "q", lazy.window.kill()),
    # Focus
    Key([MOD], "h", lazy.layout.left()),
    Key([MOD], "j", lazy.layout.down()),
    Key([MOD], "k", lazy.layout.up()),
    Key([MOD], "l", lazy.layout.right()),
    # Tabs
    Key([MOD], "t", new_group),
    Key([MOD], "w", delete_group),
    Key([MOD], "n", lazy.screen.next_group()),
    Key([MOD], "p", lazy.screen.prev_group()),
    Key([MOD, SHIFT], "n", to_next_group),
    Key([MOD, SHIFT], "p", to_prev_group),
    # Layout
    Key([MOD], "f", lazy.next_layout()),
    # # Screens
    Key([MOD], "bracketright", lazy.next_screen()),
    Key([MOD], "bracketleft", lazy.prev_screen()),
    # Shuffle
    KeyChord(
        [MOD],
        "m",
        mode=True,
        submappings=[
            Key([], "h", lazy.layout.shuffle_left()),
            Key([], "j", lazy.layout.shuffle_down()),
            Key([], "k", lazy.layout.shuffle_up()),
            Key([], "l", lazy.layout.shuffle_right()),
        ],
    ),
    # Resize
    KeyChord(
        [MOD],
        "r",
        mode=True,
        submappings=[
            Key([], "h", lazy.layout.grow_left()),
            Key([], "j", lazy.layout.grow_down()),
            Key([], "k", lazy.layout.grow_up()),
            Key([], "l", lazy.layout.grow_right()),
        ],
    ),
    # Exec
    KeyChord(
        [MOD],
        "x",
        [
            Key([], "t", lazy.spawn(TERMINAL)),
            Key([], "b", lazy.spawn(BROWSER)),
            Key([], "s", lazy.spawn(PASSWORD_MANAGER)),
            Key([], "l", lazy.spawn(LAUNCHER)),
            Key([], "e", lazy.spawn("rofimoji")),
            Key([], "u", lazy.spawn("umlaut")),
            Key([], "g", lazy.spawn("rofi-gitmojis")),
            Key([], "h", lazy.spawn("autorandr common")),
            Key([], "return", lazy.spawn("rat")),
        ],
    ),
]

# -- GROUPS --

groups = [Group("0", label="", layout="columns")]


# -- LAYOUT --


layouts = [
    layout.Max(border_width=0, border_focus=BLACK),
    layout.Columns(border_width=0, grow_amount=4, border_focus=YELLOW),
]


# -- WIDGET --


widget_defaults = {"font": FONT, "fontsize": 13, "padding": 2}
extension_defaults = widget_defaults.copy()

bar = bar.Bar(
    [
        widget.Spacer(length=4),
        widget.GroupBox(
            active=GRAY,
            highlight_method="text",
            this_current_screen_border=GREEN,
            block_highlight_text_color=WHITE,
            padding=4,
            margin=0,
        ),
        widget.Spacer(),
        widget.Clock(format="%GW%V %Y-%m-%d %H:%M:%S", foreground=GREEN),
        widget.Spacer(),
        VPN(update_interval=1),
        widget.Spacer(length=4),
        widget.Battery(
            battery_name="BAT0",
            energy_now_file="charge_now",
            energy_full_file="charge_full",
            power_now_file="current_now",
            update_delay=1,
            charge_char="↑",
            discharge_char="↓",
            unknown_char="",
            full_char="",
            not_charging_char="",
            format="{char} {percent:2.0%}⚡",
            fontsize=12,
            show_short_text=False,
        ),
        widget.Spacer(length=6),
        widget.Systray(),
    ],
    30,
    background=BLACK,
    margin=0,
)


@hook.subscribe.startup
def _():
    bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)


screens = [
    Screen(wallpaper="~/.config/wallpaper.png", wallpaper_mode="stretch", top=bar)
]

# -- MOUSE --

mouse = []
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_types = ["notification", "toolbar", "splash", "dialog"]
floating_layout = layout.Floating(
    border_focus=ACCENT_COLOR,
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="nextcloud"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
