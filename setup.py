import subprocess
import sys
import os

subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)

activate_script = os.path.join("venv", "Scripts", "activate")

subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

print("Ambiente virtual criado, ativado e requisitos instalados.")
