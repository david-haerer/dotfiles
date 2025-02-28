#!/usr/bin/zsh

# Source profile and aliasrc.
source "$HOME/.config/profile"
source "$HOME/.config/zsh/aliasrc"

# Load and export environment variables.
set -a
. $HOME/.config/zsh/zsh.env
set +a

# List files at every directory change.
function chpwd() {
	emulate -L zsh
	[[ -f .aliases ]] && . ./.aliases
	clear
	l
}

# yazi
function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

# Enable zsh syntax highlighting and auto-quoting.
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/zsh-autoquoter/zsh-autoquoter.zsh
ZAQ_PREFIXES=('git commit( [^ ]##)# -[^ -]#m' 'ssh( [^ ]##)# [^ -][^ ]#' 'spotifydl' 'audio-dl' 'caption-dl' 'video-dl' 'rn' 'music' 's' 'bm add' 'gn' 'n a' 'bs bm a' 'bs n a' 'bm a' 'n s' 'bs n s' 'bs bm s' 'bm s' 'bs s' 'n g' 'bg n g' 'bg bm g' 'bm g' 'bg g' 'yt-dlp')
ZSH_HIGHLIGHT_HIGHLIGHTERS+=(zaq)

# Enable zsh vi mode.
source ~/.config/zsh/zsh-vi-mode/zsh-vi-mode.plugin.zsh
ZVM_INSERT_MODE_CURSOR=$ZVM_CURSOR_BEAM
ZVM_NORMAL_MODE_CURSOR=$ZVM_CURSOR_BLOCK
ZVM_OPPEND_MODE_CURSOR=$ZVM_CURSOR_UNDERLINE

function apparate() {
	destination="$1"
	if [ $destination = "--help" ]; then
		apparition apparate --help
		return
	fi

	output=$(apparition apparate --called-from-shell-function "$1")

	if [ $? = 0 ]; then
		eval $output
	else
		apparition print-error "$output"
	fi
}

autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
fpath+=~/.zfunc

[[ -f .aliases ]] && . ./.aliases

# List files at shell startup.
l

# bun
[ -s "/home/david/.bun/_bun" ] && source "/home/david/.bun/_bun"
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

# Use the 'starship' prompt.
eval "$(starship init zsh)"
