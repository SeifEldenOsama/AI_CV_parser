from pyngrok import ngrok
import subprocess
import os

def start_ngrok(token, port=8501):
    os.system(f"ngrok config add-authtoken {token}")
    ngrok.kill()

    public_url = ngrok.connect(port)
    print("🔗 Public URL:", public_url)

    subprocess.Popen([
        "streamlit", "run", "app.py",
        "--server.port", str(port),
        "--server.address=0.0.0.0"
    ])
