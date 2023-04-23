import sys, os
import subprocess
imp = ['keyboard', 'pyautogui','webbrowser']
modules = []

for x in imp:
    try:
        modules.append(__import__(x))
        print(f"Found {x}.")
    except ImportError:
        print(f"{x} Not Found")
        print("Installling required packages.........")
        for x in imp:
            def install(package):
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            install(x)
        print("Packages installed successfully")
        print("Intiating the script...")

    except:
        print(f"Facing error while installing {x}")
