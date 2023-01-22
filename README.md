<p align="center">
    <h1 align="center">dotfiles</h1>
</p>

<p align="center">
    <em>Bare git repo to manage my dotfiles.</em>
</p>

## Setup

In `$HOME`, create a bare `.dotfiles.git` repository.

```bash
git init --bare .dotfiles.git
```

In `$HOME/.zshrc` (or `.bashrc`), set the `dotfiles` alias.

```bash
alias dotfiles="git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME"
```

Source the `.zshrc` to activate the new alias and hide undtracked files in the status info.

```bash
dotfiles config status.showUntrackedFiles no
```

Add the `origin` remote to the repositrory.

```bash
dotfiles remote add origin git@git.familie-haerer.de:david/dotfiles.git
```

## Usage

The `dotfiles` alias works like the normal `git` command:

* `dotfiles ls-files`: Show files tracked in the repository.
* `dotfiles status`: Show the repository status.
* `dotfiles pull`: Pull changes from remote `origin`.
* `dotfiles push`: Push changes to remote `origin`.

## Further reading

* [GitHub does dotfiles - dotfiles.github.io](https://dotfiles.github.io/)
* [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles)
* [Ask HN: What do you use to manage dotfiles?](https://news.ycombinator.com/item?id=11070797)
