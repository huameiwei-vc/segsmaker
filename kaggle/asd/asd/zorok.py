import os
import subprocess

def zzz():
    try:
        zorok = "/kaggle/working/asd/zrok/bin"
        os.makedirs(zorok, exist_ok=True)
        subprocess.run(["curl", "-sLO", "https://github.com/openziti/zrok/releases/download/v0.4.23/zrok_0.4.23_linux_amd64.tar.gz"], check=True)
        subprocess.run(["tar", "-xzf", "zrok_0.4.23_linux_amd64.tar.gz", "-C", zorok, "--wildcards", "*zrok"], check=True)
        os.remove("zrok_0.4.23_linux_amd64.tar.gz")

    except Exception as e:
        print(f"An error occurred: {e}")

zzz()
