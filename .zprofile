#!/bin/sh

source "$HOME/.config/profile"

set -a
. $HOME/.config/zsh/zsh.env
set +a

sudo loadkeys $HOME/.config/key.map
