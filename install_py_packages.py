import subprocess
import sys

packages = ["streamlit", "pandas", "matplotlib"]


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


for package in packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        install(package)
    else:
        print(f"{package} is already installed.")
