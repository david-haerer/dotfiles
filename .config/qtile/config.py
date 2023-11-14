import sh
from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy


# -- CONSTANTS --


MOD = "mod4"
ALT = "mod1"
HASHTAG = "numbersign"
TERMINAL = "wezterm"
SIGNAL = "signal-desktop"
LAUNCHER = "rofi -show drun"
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

FONT = "ComicCode Nerd Font"
L = lazy.layout


# -- AUTOSTART --


def ensure_running(proc_name, run_proc):
    try:
        sh.pidof(proc_name)
    except sh.ErrorReturnCode:
        run_proc()


@hook.subscribe.startup
def autostart():
    lambda: sh.autorandr("common")
    lambda: sh.setx()
    lambda: sh.flameshot()
    ensure_running("nm-applet", lambda: sh.nm_applet(_bg=True))
    ensure_running("nextcloud", lambda: sh.nextcloud(_bg=True))


# -- KEYS --


keys = []

keys.extend(
    [
        Key([MOD, ALT], "h", L.left(), desc="Move focus to left"),
        Key([MOD, ALT], "l", L.right(), desc="Move focus to right"),
        Key([MOD, ALT], "j", L.down(), desc="Move focus down"),
        Key([MOD, ALT], "k", L.up(), desc="Move focus up"),
    ]
)

keys.extend(
    [
        Key([MOD, "shift"], "h", L.shuffle_left(), desc="Move window to the left"),
        Key([MOD, "shift"], "l", L.shuffle_right(), desc="Move window to the right"),
        Key([MOD, "shift"], "j", L.shuffle_down(), desc="Move window down"),
        Key([MOD, "shift"], "k", L.shuffle_up(), desc="Move window up"),
    ]
)

keys.extend(
    [
        Key([MOD, "control"], "h", L.grow_left(), desc="Grow window to the left"),
        Key([MOD, "control"], "l", L.grow_right(), desc="Grow window to the right"),
        Key([MOD, "control"], "j", L.grow_down(), desc="Grow window down"),
        Key([MOD, "control"], "k", L.grow_up(), desc="Grow window up"),
    ]
)

keys.extend(
    [
        Key([MOD], "tab", lazy.screen.next_group(), desc="Switch to next group"),
        Key(
            [MOD, "shift"],
            "tab",
            lazy.screen.prev_group(),
            desc="Switch to previous group",
        ),
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
        Key([MOD], "n", L.normalize(), desc="Reset all window sizes"),
        Key([MOD, "shift"], "return", L.toggle_split(), desc="Toggle (un-)split"),
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
        Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        Key(
            [], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 6- unmute")
        ),
        Key(
            [], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 6+ unmute")
        ),
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

groups.append(
    ScratchPad(
        "scratchpad",
        dropdowns=[
            DropDown("term", "alacritty"),
        ],
    )
)

keys.extend(
    [
        # Key([MOD], "tab", lazy.function(Client.cycle_groups())),
        Key([MOD], "t", lazy.spawn(TERMINAL), desc="Launch terminal"),
        Key([MOD], "s", lazy.spawn(SIGNAL), desc="Launch Signal"),
        Key(
            [MOD],
            HASHTAG,
            lazy.spawn(PASSWORD_MANAGER),
            desc="Launch password manager",
        ),
        Key([MOD], "return", lazy.spawn(LAUNCHER), desc="Application launcher"),
        Key([MOD], "r", lazy.spawncmd(), desc="Command prompt"),
        Key([MOD], "space", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([MOD], "u", lazy.spawn("rofimoji"), desc="Launch unicode picker"),
        Key([MOD], "h", lazy.spawn("autorandr common"), desc="Launch unicode picker"),
    ]
)


# -- LAYOUT --


layouts = [
    layout.Columns(
        border_on_single=True,
        border_focus=ACCENT_COLOR,
        border_focus_stack=ACCENT_COLOR,
        border_width=1,
        grow_amount=6,
        margin=0,
    ),
    layout.Max(),
]


# -- WIDGET --


widget_defaults = dict(
    font=FONT,
    fontsize=13,
    padding=2,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Nextcloud/Bilder/Hintergründe/wallpaper.png",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=GRAY,
                    highlight_method="text",
                    this_current_screen_border=GREEN,
                    block_highlight_text_color=BLACK,
                    padding=4,
                    margin=0,
                    hide_unused=True,
                ),
                widget.Spacer(),
                widget.Clock(format="%Y-%m-%d %H:%M", foreground=GREEN),
                widget.Spacer(),
                widget.Systray(),
                widget.Spacer(length=8),
                widget.Battery(
                    battery_name="BAT0",
                    energy_now_file="charge_now",
                    energy_full_file="charge_full",
                    power_now_file="current_now",
                    update_delay=1,
                    charge_char="↑",
                    discharge_char="↓",
                    format="{char} {percent:2.0%}",
                    fontsize=12,
                ),
                widget.Spacer(length=8),
                widget.LaunchBar(
                    progs=[
                        ("🔒", "sudo loginctl terminate-user 1000"),
                        ("❌", "sudo shutdown -h now"),
                    ],
                ),
            ],
            30,
            background=BLACK,
            opacity=0.66,
        ),
    ),
]


# -- MOUSE --


mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=ACCENT_COLOR,
    border_width=1,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
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
