#!/usr/bin/python3
import subprocess
import argparse


parser = argparse.ArgumentParser(description="up - An Arch Linux Update utility")
parser.add_argument("-r", "--repo", action="store_true", help="Update Repo packages")
parser.add_argument("-a", "--aur", action="store_true", help="Update AUR packages")
parser.add_argument("-f", "--flatpak", action="store_true", help="Update flatpaks")
parser.add_argument("-i", "--idle", action="store_true", help="Will not ask for confirmation")

args = parser.parse_args()


GREEN = "\033[32m"
RESET = "\033[0m"
SEPARATOR = f"{GREEN}{'-' * 100}{RESET}"

idle = False
if not (args.repo or args.aur or args.flatpak):
    # -------------------------
    #     UPDATE SELECTION
    # -------------------------
    print("Select what to update")
    print("1) Everything (Repo - AUR - Flatpak)")
    print("2) Group  - Repo - AUR")
    print("3) Single - Repo")
    print("4) Single - AUR")
    print("5) Single - Flatpak only")
    print("6) Exit")

    while True:
        update = input("Select [1-6] ").strip()

    # -------------------------
    #     SELECTION LOGIC
    # -------------------------
        if update == "1":
            repo = True
            aur = True
            flatpak = True
            break
        elif update == "2":
            repo = True
            aur = True
            flatpak = False
            break
        elif update == "3":
            repo = True
            aur = False
            flatpak = False
            break
        elif update == "4":
            repo = False
            aur = True
            flatpak = False
            break
        elif update == "5":
            repo = False
            aur = False
            flatpak = True
            break
        elif update == "6":
            exit(0)

    # -------------------------
    #    IDLE MODE SELECTION
    # -------------------------
    print("Idle mode? (Will not ask for confirmation)")
    while True:
        answer = input("[y/N] ").strip().lower()
        if answer in ("y", "yes"):
            idle = True
            break
        elif answer in ("n", "no", ""):
            idle = False
            break
else:
    repo = args.repo
    aur = args.aur
    flatpak = args.flatpak
    idle = args.idle
    print(f"{GREEN}==> Arguments detected - Skipping menu{RESET}")


# -------------------------
#       UPDATE LOGIC
# -------------------------

print(SEPARATOR)
if repo:
    # -------------------------
    #       REPO UPGRADE
    # -------------------------
    print(f"{GREEN}==> Running repo upgrade...{RESET}")
    if idle:
        subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
    else:
        subprocess.run(["sudo", "pacman", "-Syu"])
    print(SEPARATOR)

if aur:
    # -------------------------
    #       AUR UPGRADE
    # -------------------------
    print(f"{GREEN}==> Running AUR upgrade...{RESET}")
    if idle:
        subprocess.run(["paru", "-Sua", "--noconfirm"])
    else:
        subprocess.run(["paru", "-Sua"])
    print(SEPARATOR)

if flatpak:
    # -------------------------
    #      FLATPAK UPGRADE
    # -------------------------
    print(f"{GREEN}==> Running flatpak upgrade...{RESET}")
    if idle:
        subprocess.run(["flatpak", "update", "-y"])
    else:
        subprocess.run(["flatpak", "update"])
    print(SEPARATOR)
