import os

from libqtile import bar, hook, layout, widget
from libqtile.config import DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.widget import base


class VPN(base.InLoopPollText):
    def poll(self):
        return ""
        # return "VPN" if sh.mullvad("status").startswith("Connected") else ""


# -- CONSTANTS --

MOD = "mod4"
ALT = "mod1"
ALTGR = "mod5"
HASHTAG = "numbersign"
CTRL = "control"
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

L = lazy.layout


# -- AUTOSTART --


def ensure_running(proc_name, run_proc):
    return
    # try:
    #     sh.pidof(proc_name)
    # except sh.ErrorReturnCode:
    #     run_proc()


@hook.subscribe.startup
def autostart():
    # lambda: sh.autorandr("common")
    # ensure_running("nm-applet", lambda: sh.nm_applet(_bg=True))
    # ensure_running("nextcloud", lambda: sh.nextcloud(_bg=True))
    # ensure_running("flameshot", lambda: sh.flameshot(_bg=True))
    # ensure_running("blueman-applet", lambda: sh.blueman_applet(_bg=True))
    return


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


# -- KEYS --

keys = []

keys.extend(
    [
        Key([MOD, ALT], "h", L.left(), desc="Move focus to left"),
        Key([MOD, ALT], "l", L.right(), desc="Move focus to right"),
        Key([MOD, ALT], "j", L.down(), desc="Move focus down"),
        Key([MOD, ALT], "k", L.up(), desc="Move focus up"),
        Key([MOD, "control"], "h", L.left(), desc="Move focus to left"),
        Key([MOD, "control"], "l", L.right(), desc="Move focus to right"),
        Key([MOD, "control"], "j", L.down(), desc="Move focus down"),
        Key([MOD, "control"], "k", L.up(), desc="Move focus up"),
    ]
)

keys.extend(
    [
        Key(
            [MOD, "control", "shift"],
            "h",
            L.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [MOD, "control", "shift"],
            "l",
            L.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([MOD, "control", "shift"], "j", L.shuffle_down(), desc="Move window down"),
        Key([MOD, "control", "shift"], "k", L.shuffle_up(), desc="Move window up"),
    ]
)

keys.extend(
    [
        Key([MOD, "shift"], "h", L.grow_left(), desc="Grow window to the left"),
        Key([MOD, "shift"], "l", L.grow_right(), desc="Grow window to the right"),
        Key([MOD, "shift"], "j", L.grow_down(), desc="Grow window down"),
        Key([MOD, "shift"], "k", L.grow_up(), desc="Grow window up"),
    ]
)

keys.extend(
    [
        Key([MOD], "n", lazy.screen.next_group(), desc="Switch to next group"),
        Key([MOD], "p", lazy.screen.prev_group(), desc="Switch to previous group"),
        Key([MOD], "comma", lazy.next_screen(), desc="Switch to next screen"),
        Key(
            [MOD, "shift"],
            "comma",
            lazy.prev_screen(),
            desc="Switch to previous screen",
        ),
    ]
)

keys.extend(
    [
        Key([MOD], "m", lazy.next_layout(), desc="Toggle between layouts"),
        Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ]
)

keys.extend(
    [
        Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master toggle")),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("amixer -D pulse sset Master 7%- unmute"),
        ),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("amixer -D pulse sset Master 7%+ unmute"),
        ),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    ]
)

# -- GROUPS --

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )


W, H = 0.9975, 1.035
DX, DY = 0.0005, -0.038
cos30, sin30 = 0.8660254037844387, 0.5
width, height = cos30 * W, sin30 * H
x, y = (1 - cos30) / 2 * W + DX, (1 - sin30) / 2 * H + DY

groups.append(
    ScratchPad(
        "scratchpad",
        dropdowns=[DropDown("term", TERMINAL, width=width, height=height, x=x, y=y)],
    )
)

keys.extend(
    [
        Key([MOD], "t", lazy.spawn(TERMINAL), desc="Launch terminal"),
        Key([MOD], "s", lazy.spawn(SIGNAL), desc="Launch Signal"),
        Key([MOD], "b", lazy.spawn(BROWSER), desc="Launch Browser"),
        Key([MOD], "s", lazy.spawn(PASSWORD_MANAGER), desc="Launch password manager"),
        Key([MOD], "period", lazy.spawn(LAUNCHER), desc="Application launcher"),
        Key([MOD], "space", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([MOD], "e", lazy.spawn("rofimoji"), desc="Launch unicode picker"),
        Key([MOD], "u", lazy.spawn("umlaut"), desc="Launch umlaut picker"),
        Key([MOD], "g", lazy.spawn("rofi-gitmojis"), desc="Launch Gitmoji picker"),
        Key([MOD], "h", lazy.spawn("autorandr common"), desc="Launch unicode picker"),
        Key([MOD], "return", lazy.spawn("rat"), desc="Launch the rat"),
    ]
)


# -- LAYOUT --


layouts = [
    layout.Max(margin=0),
    layout.Columns(
        border_on_single=True,
        border_focus=ACCENT_COLOR,
        border_focus_stack=ACCENT_COLOR,
        border_width=2,
        grow_amount=6,
        margin=4,
    ),
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
            hide_unused=True,
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
        widget.Spacer(length=6),
        widget.LaunchBar(
            progs=[
                ("🔒", f"sudo loginctl terminate-user {USER}"),
                ("❌", "sudo shutdown -h now"),
            ]
        ),
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
