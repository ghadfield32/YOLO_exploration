import os
import requests

def download_weights():
    weights_dir = os.path.join("weights")
    os.makedirs(weights_dir, exist_ok=True)

    weights_urls = [
        "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt",
        "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10s.pt",
        "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10m.pt",
        "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10b.pt",
        "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10x.pt",
        "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10l.pt"
    ]

    def download_file(url, dest_folder):
        filename = os.path.join(dest_folder, url.split('/')[-1])
        if not os.path.exists(filename):
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"File already exists: {filename}")

    for url in weights_urls:
        download_file(url, weights_dir)
