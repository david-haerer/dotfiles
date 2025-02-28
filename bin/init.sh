#!/bin/sh

git config --global init.defaultBranch main
git init --bare .dotfiles.git
alias dot="git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME"
dot config status.showUntrackedFiles no
dot remote add origin git@github.com:david-haerer/dotfiles.git \
    || dot remote add origin https://github.com/DavidHeresy/dotfiles.git
