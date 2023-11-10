<p align="center">
    <h1 align="center">dotfiles</h1>
</p>

<p align="center">
    <em>Bare git repo to manage my dotfiles.</em>
</p>

## Requirements

Curl and git must be installed and to push changes an SSH key must be added to GitHub.

## Setup

In `$HOME` execute the following command:

```bash
curl -sSL https://dotfiles.haerer.dev | sh
alias dot=""
dot pull
```

## Usage

The `dot` alias works like the normal `git` command.

## Git

Include the `.config/git/.gitconfig` in you `$HOME/.gitconfig` with


## Further reading

* [GitHub does dotfiles - dotfiles.github.io](https://dotfiles.github.io/)
* [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles)
* [Ask HN: What do you use to manage dotfiles?](https://news.ycombinator.com/item?id=11070797)
