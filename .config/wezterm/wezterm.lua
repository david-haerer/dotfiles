local wezterm = require("wezterm")

local FONT = os.getenv("FONT")

local BLACK = "#0A0E14"
local GRAY = "#4D5566"
local WHITE = "#B3B1AD"
local RED = "#FF3333"
local ORANGE = "#E6B450"
local YELLOW = "#FF8F40"
local GREEN = "#C2D94C"
local CYAN = "#95E6CB"
local BLUE = "#59C2FF"
local MAGENTA = "#FFEE99"

local config = {}

-- config.window_background_opacity = 0.9
config.color_scheme = "Ayu Dark (Gogh)"
config.use_fancy_tab_bar = false
config.hide_tab_bar_if_only_one_tab = true

config.font = wezterm.font_with_fallback({ FONT, "FiraCode Nerd Font", "Noto Sans Mono CJK SC" })

config.window_frame = {
	font = wezterm.font({ family = "ComicCodeLigatures Nerd Font", weight = "Bold" }),
	font_size = 12.0,
}

config.colors = {
	tab_bar = {
		background = BLACK,
		active_tab = { bg_color = BLACK, fg_color = YELLOW, intensity = "Bold" },
		inactive_tab = { bg_color = BLACK, fg_color = GRAY },
		inactive_tab_hover = { bg_color = BLACK, fg_color = WHITE },
		new_tab = { bg_color = BLACK, fg_color = GRAY },
		new_tab_hover = { bg_color = BLACK, fg_color = WHITE },
	},
}

config.force_reverse_video_cursor = true
config.disable_default_key_bindings = true

config.keys = {
	{ mods="SUPER", key= "c", action = wezterm.action.CopyTo("Clipboard")},
	{ mods="SUPER", key= "v", action = wezterm.action.PasteFrom("Clipboard")},
	
	{ mods="CTRL", key = "n", action = wezterm.action.ActivateTabRelative(1) },
	{ mods="CTRL", key = "p", action = wezterm.action.ActivateTabRelative(-1) },

	{ mods="CTRL", key = "h", action = wezterm.action.ActivatePaneDirection("Left") },
	{ mods="CTRL", key = "j", action = wezterm.action.ActivatePaneDirection("Down") },
	{ mods="CTRL", key = "k", action = wezterm.action.ActivatePaneDirection("Up") },
	{ mods="CTRL", key = "l", action = wezterm.action.ActivatePaneDirection("Right") },

	{ mods="CTRL", key = "t", action = wezterm.action.SpawnTab("CurrentPaneDomain") },
	{ mods="CTRL", key = "f", action = wezterm.action.TogglePaneZoomState },
	{ mods="CTRL", key = "v", action = wezterm.action.SplitHorizontal({ domain = "CurrentPaneDomain" }) },
	{ mods="CTRL", key = "s", action = wezterm.action.SplitVertical({ domain = "CurrentPaneDomain" }) },
	{ mods="CTRL", key = "r", action = wezterm.action.ActivateKeyTable({ name = "resize", one_shot = false }) },
}

config.key_tables = {
	resize = {
		{ key = "h", action = wezterm.action.AdjustPaneSize({ "Left", 1 }) },
		{ key = "j", action = wezterm.action.AdjustPaneSize({ "Down", 1 }) },
		{ key = "k", action = wezterm.action.AdjustPaneSize({ "Up", 1 }) },
		{ key = "l", action = wezterm.action.AdjustPaneSize({ "Right", 1 }) },
		{ key = "Escape", action = "PopKeyTable" },
	},
}

return config
