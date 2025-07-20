import subprocess
import sys
import os

python_path = sys.executable

script_path = os.path.abspath(r"D:\Tasks\Llm-Chatbot\app.py")

subprocess.run([python_path, "-m", "streamlit", "run", script_path])
