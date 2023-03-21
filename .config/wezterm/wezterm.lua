local wezterm = require 'wezterm'

return {
  color_scheme = "SeaShells",

  font = wezterm.font_with_fallback {
    "ComicCodeLigatures Nerd Font",
    "FiraCode Nerd Font",
  },

  keys = {
    {
      key = 'w',
      mods = 'CTRL',
      action = wezterm.action.CloseCurrentTab { confirm = true },
    },
  },
}
