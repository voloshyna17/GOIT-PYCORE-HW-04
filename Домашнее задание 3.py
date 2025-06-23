import sys
from pathlib import Path
from colorama import init, Fore 

init()

def print_directory_tree(path: Path, prefix=""):
    try:
        for item in sorted (path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/{Fore.RESET}")
                print_directory_tree(item,prefix+"   ")
            else:
                print(f"{prefix}{Fore.BLUE}{item.name}/{Fore.RESET}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission denied]{Fore.RESET}")

def main():
    if len(sys.argv)<2:
        print("Вкажіть шлях до директорії як аргумент")
        return
    dir_path=Path(sys.argv[1])
    if not dir_path.exists():
        print("Шлях не існує")
        return
    if not dir_path.is_dir():
        print("Це не директорія")
        return
    print(f"{Fore.MAGENTA}{dir_path.name}/{Fore.RESET}")
    print_directory_tree(dir_path)


if __name__=="__main__":
    main()