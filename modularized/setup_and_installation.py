import subprocess

def setup_and_install():
    # Install necessary packages
    packages = [
        "git+https://github.com/THU-MIG/yolov10.git",
        "supervision",
        "roboflow"
    ]

    for package in packages:
        subprocess.run(["pip", "install", package], check=True)

    print("Setup and installation complete.")
