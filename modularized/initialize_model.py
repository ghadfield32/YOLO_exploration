import torch
from ultralytics import YOLOv10
import os

def initialize_model(weights_dir):
    print(torch.__version__)
    print("CUDA available: ", torch.cuda.is_available())
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    model = YOLOv10(os.path.join(weights_dir, "yolov10n.pt"))
    print("yolov10 preset classes = ", model.names)
    return model, device
