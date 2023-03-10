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


# Set window title.
function set-title() {
    print -Pn "\e]2;$USER@$(hostname | sd '\..*' '')$(pwd)\a" # Set window title.
}

# List files at every directory change.
function chpwd() {
    clear
    emulate -L zsh
    set-title
    l
}

# Enable zsh syntax highlighting and auto-quoting.
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/zsh-autoquoter/zsh-autoquoter.zsh
ZAQ_PREFIXES=('git commit( [^ ]##)# -[^ -]#m' 'ssh( [^ ]##)# [^ -][^ ]#' 'spotifydl' 'audio-dl' 'caption-dl' 'video-dl' 'rn' 'music' 's')
ZSH_HIGHLIGHT_HIGHLIGHTERS+=(zaq)

# Use the 'starship' prompt.
eval "$(starship init zsh)"

################################################################################
# Shell function for safe use of `apparition apparate`.
# Arguments:
#     $1: The destination name passed to `apparition apparate`
#         If the value is `--help` only the help text is shown.
#         Otherwise the command is executed with `eval`.
# Outputs:
#     Writes error messages to STDERR.
################################################################################
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
zstyle ':completion:*' menu select
fpath+=~/.zfunc

# List files at shell startup.
set-title
l
