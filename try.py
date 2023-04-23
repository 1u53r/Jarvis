import sys, os
import subprocess
imp = ['speech_recognition', 'googletrans','pyaudio'] # package name to import, name should be exact as fro import. 
pack = ['SpeechRecognition','googletrans==3.1.0a0','PyAudio'] ###name of package to install package ## Note the package name should be exact as the command requires for pip 
modules = []

for x in imp:
    try:
        modules.append(__import__(x))
        print(f"Found {x}.")
    except ImportError:
        print(f"{x} Not Found")
        print("Installling required packages.........")
        for x in pack:
            def install(package):
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            install(x)
        print("Packages installed successfully")
        print("Intiating the script...")

    except:
        print(f"Facing error while installing {x}")
