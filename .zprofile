#!/bin/sh

source "$HOME/.config/profile"

set -a
. $HOME/.config/zsh/zsh.env
set +a

if [ -z "$DISPLAY" ] && [ "$XDG_VTNR" = 1 ]; then
  exec startx
fi
