<p align="center">
  <h1 align="center">dotfiles</h1>
</p>

<p align="center">
  <em>🏡 Furnishings of my <code>$HOME</code>.</em>
</p>

## Requirements

- `git` must be installed.
- To push changes an SSH key must be added to GitHub.

## Setup

In `$HOME` execute the following command:

1. Clone the repo
   ```sh
   git clone git@github.com:david-haerer/dotfiles.git
   ```
   or
   ```sh
   git clone https://github.com/david-haerer/dotfiles.git
   ```
2. Copy the `.git` folder
   ```sh
   cp $HOME/dotfiles/.git $HOME/.dotfiles.git
   ```
3. Set the dot alias.
   ```sh
   alias dot="git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME"
   ```
4. Restore the working directory.
   ```sh
   dot restore $HOME
   ```

## Usage

The `dot` alias works like the normal `git` command.

## Git

Include the `.config/git/.gitconfig` in you `$HOME/.gitconfig` with

## Further reading

- [GitHub does dotfiles - dotfiles.github.io](https://dotfiles.github.io/)
- [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles)
- [Ask HN: What do you use to manage dotfiles?](https://news.ycombinator.com/item?id=11070797)
