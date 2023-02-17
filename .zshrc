# Use vi mode.
bindkey -v

# Load and export setting variables.
set -a
. $HOME/.config/sh/setting.env
set +a

# Source various profiles.
source "$HOME/profile"
source "$HOME/.config/sh/aliasrc"
export PATH="$HOME/.scripts:$PATH"
export PATH="$HOME/.poetry/bin:$PATH"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# List files at every directory change.
function chpwd() {
    clear
    emulate -L zsh
    l
}

# Enable zsh syntax highlighting.
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Enable zsh autoquoter.
source ~/.config/zsh/zsh-autoquoter/zsh-autoquoter.zsh
ZAQ_PREFIXES=('git commit( [^ ]##)# -[^ -]#m' 'ssh( [^ ]##)# [^ -][^ ]#' 'spotifydl' 'audio-dl' 'caption-dl' 'video-dl' 'rn' 'music' 's')
ZSH_HIGHLIGHT_HIGHLIGHTERS+=(zaq)

# Use the 'starship' prompt.
eval "$(starship init zsh)"

# List files to start working.
l

