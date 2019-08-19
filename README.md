# PyMiltank
A Python port of https://github.com/dfrankland/pokemonsay with minimal dependencies.

This project aims to provide tools to convert existing assets into cowsay templates. Instead of cloning cowsay, why not just assimilate it with Pokemon instead?

# Installing
```bash
python3 -m venv .pyenv
. .pyenv/bin/activate
pip3 install -r requirements.txt
```

# Getting sprites
You can grab sprites from the original inspiration ([pokesay](https://github.com/dfrankland/pokemonsay)) or from the [Veekun Pokedex's media repository](http://git.veekun.com/pokedex-media.git)

When cloning from the Veekun GIT, use `--depth 1` to make a shallow clone, there is quite a bit of stuff on there:
```bash
$ git clone --depth 1 git://git.veekun.com/pokedex-media.git assets
Cloning into 'assets'...
remote: Counting objects: 53554, done.
remote: Compressing objects: 100% (51005/51005), done.
remote: Total 53554 (delta 2547), reused 52849 (delta 2527)
Receiving objects: 100% (53554/53554), 504.65 MiB | 2.91 MiB/s, done.
Resolving deltas: 100% (2547/2547), done.
Checking out files: 100% (59086/59086), done.
```

The icons to use will be under `pokemon/icons`, any other larger graphics will look like crap when "pixelized".