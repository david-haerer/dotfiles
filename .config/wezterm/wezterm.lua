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
      mods = 'CMD',
      action = wezterm.action.CloseCurrentTab { confirm = true },
    },
  },
}
