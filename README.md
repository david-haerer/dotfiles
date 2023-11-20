<p align="center">
  <h1 align="center">dotfiles</h1>
</p>

<p align="center">
  <em>🏡 Furnishings of my <code>$HOME</code>.</em>
</p>

## Requirements

`curl` and `git` must be installed.
To push changes an SSH key must be added to GitHub.

## Setup

In `$HOME` execute the following command:

```sh
curl -sSL https://dotfiles.haerer.dev | sh
alias dot="git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME"
dot pull
```

Once you have your SSH key setup, you have to change the remote URL:

```sh
dot-update-remote-url
```

Install a basic set of dependencies with:

```sh
setup
```

## Usage

The `dot` alias works like the normal `git` command.

## Git

Include the `.config/git/.gitconfig` in you `$HOME/.gitconfig` with

## Further reading

* [GitHub does dotfiles - dotfiles.github.io](https://dotfiles.github.io/)
* [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles)
* [Ask HN: What do you use to manage dotfiles?](https://news.ycombinator.com/item?id=11070797)
