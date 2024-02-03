local wezterm = require 'wezterm'

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

  
config.window_background_opacity = 0.9
config.color_scheme = "Ayu Dark (Gogh)"
config.use_fancy_tab_bar = false
config.hide_tab_bar_if_only_one_tab = true

config.font = wezterm.font_with_fallback {
  FONT,
  "FiraCode Nerd Font",
  "Noto Sans Mono CJK SC",
}

config.window_frame = {
    font = wezterm.font { family = 'ComicCodeLigatures Nerd Font', weight = 'Bold' },
    font_size = 12.0,
}


config.colors = {
  cursor_bg = ORANGE,
  cursor_fg = BLACK,
  cursor_border = ORANGE,
  tab_bar = {
    background = BLACK,
    active_tab = {
      bg_color = BLACK,
      fg_color = YELLOW,
      intensity = "Bold",
    },
    inactive_tab = {
      bg_color = BLACK,
      fg_color = GRAY,
    },
    inactive_tab_hover = {
      bg_color = BLACK,
      fg_color = WHITE,
    },
    new_tab = {
      bg_color = BLACK,
      fg_color = GRAY,
    },
    new_tab_hover = {
      bg_color = BLACK,
      fg_color = WHITE,
    },
  } 
}

config.term = "wezterm"

config.force_reverse_video_cursor = true

return config
