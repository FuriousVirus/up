# up - An Arch Linux update utility

Update all your packages in one command

## Installation
### Requirements
A mutable Arch Linux based system with paru, Flatpak and Python3

> [!WARNING]
> Not compatible with SteamOS due to its immutability

### Install system-wide
```bash
git clone https://github.com/FuriousVirus/up.git
cd up
sudo cp up.py /usr/local/bin/up
```

### Install for user
```bash
git clone https://github.com/FuriousVirus/up.git
cd up
mkdir -p $HOME/.local/bin
cp up.py $HOME/.local/bin/up
```
Make sure ~/.local/bin is in your $PATH if you use the user install

## Usage
### CLI Flags
| Short | Long | Description|
|-------|-----------|-------------------------------|
| -r | --repo | Update Repo packages|
| -a | --aur  | Update AUR packages with paru|
| -f| --flatpak | Update flatpaks|
| -i| --idle| Don't ask for confirmation |

### Examples
  ```bash
  up          # interactive update menu
  up -raf     # update repo + AUR + flatpak, with confirmation
  up -rafi    # same, no prompts
  up -f       # update Flatpaks only
  ```

## License
GPLv3, see [LICENSE](LICENSE).