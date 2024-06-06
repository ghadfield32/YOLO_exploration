import os
import shutil

def custom_training(weights_dir, data_yaml_path, device, epochs, batch_size):
    runs_dir = os.path.join("runs")
    if os.path.exists(runs_dir):
        shutil.rmtree(runs_dir)
        print(f"Removed previous run files in {runs_dir}")

    os.system(f'yolo task=detect mode=train epochs={epochs} batch={batch_size} plots=True model={os.path.join(weights_dir, "yolov10x.pt")} data={data_yaml_path} device={device}')
