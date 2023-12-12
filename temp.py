from Genration_Of_Images import Generate_Images , Show_Image
from func.Speak.SpeakOffline import Speak
import subprocess

# Install C++ using Chocolatey
subprocess.run(["choco", "install", "cpp"], capture_output=True, text=True)

# Install Hindi language pack using Chocolatey
subprocess.run(["choco", "install", "hindi"], capture_output=True, text=True)