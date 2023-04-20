
from contextlib import contextmanager
import sys, os
import subprocess
imp = ['scipy', 'pytorch', 'keras', 'seaborn']
modules = []

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

for x in imp:
    try:
        modules.append(__import__(x))
        print(f"Found {x}.")
    except ImportError:
        print(f"{x} Not Found")
        print("Installling required packages.........")
        with suppress_stdout():
            for x in imp:
                
                def install(package):
                        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                install(x)
        print("Packages installed successfully")
        print("Intiating the script...")