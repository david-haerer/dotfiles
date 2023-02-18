# Use vi mode.
bindkey -v

# Source profile and aliasrc.
source "$HOME/profile"
source "$HOME/.config/zsh/aliasrc"

# Load and export environment variables.
set -a
. $HOME/.config/zsh/zsh.env
set +a

# Setup nvm.
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# List files at every directory change.
function chpwd() {
    clear
    emulate -L zsh
    print -Pn "\e]2;$(pwd)\a" # Set window title.
    l
}

# Enable zsh syntax highlighting and auto-quoting.
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/zsh-autoquoter/zsh-autoquoter.zsh
ZAQ_PREFIXES=('git commit( [^ ]##)# -[^ -]#m' 'ssh( [^ ]##)# [^ -][^ ]#' 'spotifydl' 'audio-dl' 'caption-dl' 'video-dl' 'rn' 'music' 's')
ZSH_HIGHLIGHT_HIGHLIGHTERS+=(zaq)

# Use the 'starship' prompt.
eval "$(starship init zsh)"

# List files at shell startup.
print -Pn "\e]2;$(pwd)\a" # Set window title.
l

