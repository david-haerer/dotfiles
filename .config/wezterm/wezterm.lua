local wezterm = require 'wezterm'


return {
  color_scheme = "Ayu Dark (Gogh)",

  font = wezterm.font_with_fallback {
    "ComicCodeLigatures Nerd Font",
    "FiraCode Nerd Font",
    "Noto Sans Mono CJK SC",
  },

  window_frame = {
    font = wezterm.font { family = 'ComicCodeLigatures Nerd Font', weight = 'Bold' },
    font_size = 12.0,
  },
}
