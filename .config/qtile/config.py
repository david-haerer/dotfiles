from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy


# -- CONSTANTS --


MOD = "mod4"
TERMINAL = "wezterm"
SIGNAL = "/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=signal-desktop --file-forwarding org.signal.Signal @@u %U @@"
LAUNCHER = "rofi -show drun"
PASSWORD_MANAGER = "passmenu"
ACCENT_COLOR = "#008abd"
FONT = "ComicCode Nerd Font"
L = lazy.layout


# -- KEYS --


keys = []

keys.extend(
    [
        Key([MOD], "h", L.left(), desc="Move focus to left"),
        Key([MOD], "l", L.right(), desc="Move focus to right"),
        Key([MOD], "j", L.down(), desc="Move focus down"),
        Key([MOD], "k", L.up(), desc="Move focus up"),
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
        Key([MOD], "n", L.normalize(), desc="Reset all window sizes"),
        Key([MOD, "shift"], "Return", L.toggle_split(), desc="Toggle (un-)split"),
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
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

groups.append(
    ScratchPad(
        "scratchpad",
        dropdowns=[
            DropDown("term", "alacritty", config={"opacity": 0.8}),
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
            "numbersign",
            lazy.spawn(PASSWORD_MANAGER),
            desc="Launch password manager",
        ),
        Key([MOD], "return", lazy.spawn(LAUNCHER), desc="Application launcher"),
        Key([MOD], "r", lazy.spawncmd(), desc="Command prompt"),
        Key([MOD], "space", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([MOD], "u", lazy.spawn("rofimoji"), desc="Launch unicode picker"),
    ]
)


# -- LAYOUT --


layouts = [
    layout.Columns(
        border_on_single=True,
        border_focus=ACCENT_COLOR,
        border_focus_stack=ACCENT_COLOR,
        border_width=2,
        grow_amount=6,
        margin=2,
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
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(format="%Y-%m-%d %H:%M", foreground=ACCENT_COLOR),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.BatteryIcon(),
                widget.Systray(),
                widget.QuickExit(),
            ],
            30,
        ),
    ),
    Screen(
        wallpaper="~/Nextcloud/Bilder/Hintergründe/wallpaper.png",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(format="%Y-%m-%d %H:%M", foreground=ACCENT_COLOR),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.BatteryIcon(),
                widget.Systray(),
                widget.QuickExit(),
            ],
            30,
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
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
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
