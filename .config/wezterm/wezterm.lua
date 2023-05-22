local wezterm = require 'wezterm'


return {
  color_scheme = "SeaShells",

  font = wezterm.font_with_fallback {
    "ComicCodeLigatures Nerd Font",
    "FiraCode Nerd Font",
    "Noto Sans Mono CJK SC",
  },

  -- line_height = 0.9,

  window_frame = {
    font = wezterm.font { family = 'ComicCodeLigatures Nerd Font', weight = 'Bold' },
    font_size = 12.0,
  },

  keys = {
    {
      key = "t",
      mods = "CTRL",
      action = wezterm.action{SpawnTab="CurrentPaneDomain"},
    },
    {
      key = "w",
      mods = "CTRL",
      action = wezterm.action{CloseCurrentTab={confirm=false}},
    },
  },
}
