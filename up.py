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
CYAN = "\033[36m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
SEPARATOR = f"{'-' * 50}"

idle = False
if not (args.repo or args.aur or args.flatpak):
    # -------------------------
    #     UPDATE SELECTION
    # -------------------------
    print(SEPARATOR)
    print(f"{BOLD}  Select what to update{RESET}")
    print(SEPARATOR)
    print(f"  {CYAN}1){RESET} Everything      {DIM}Repo - AUR - Flatpak{RESET}")
    print(f"  {CYAN}2){RESET} Arch only       {DIM}Repo - AUR{RESET}")
    print(f"  {CYAN}3){RESET} Repo only")
    print(f"  {CYAN}4){RESET} AUR only")
    print(f"  {CYAN}5){RESET} Flatpak only")
    print(f"  {CYAN}6){RESET} Exit")
    print(SEPARATOR)

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

print(f"{GREEN}{SEPARATOR}{RESET}")
if repo:
    # -------------------------
    #       REPO UPGRADE
    # -------------------------
    print(f"{GREEN}==> Running repo upgrade...{RESET}")
    if idle:
        subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
    else:
        subprocess.run(["sudo", "pacman", "-Syu"])
    print(f"{GREEN}{SEPARATOR}{RESET}")

if aur:
    # -------------------------
    #       AUR UPGRADE
    # -------------------------
    print(f"{GREEN}==> Running AUR upgrade...{RESET}")
    if idle:
        subprocess.run(["paru", "-Sua", "--noconfirm"])
    else:
        subprocess.run(["paru", "-Sua"])
    print(f"{GREEN}{SEPARATOR}{RESET}")

if flatpak:
    # -------------------------
    #      FLATPAK UPGRADE
    # -------------------------
    print(f"{GREEN}==> Running flatpak upgrade...{RESET}")
    if idle:
        subprocess.run(["flatpak", "update", "-y"])
    else:
        subprocess.run(["flatpak", "update"])
    print(f"{GREEN}{SEPARATOR}{RESET}")