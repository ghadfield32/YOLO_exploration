import yaml
from roboflow import Roboflow
import os

def download_dataset():
    rf = Roboflow(api_key="YOUR_API_KEY")
    project = rf.workspace("basketball-formations").project("basketball-and-hoop-7xk0h")
    version = project.version(11)
    dataset = version.download("yolov8")

    dataset_location = dataset.location
    data_yaml_path = os.path.join(dataset_location, "data.yaml")

    with open(data_yaml_path, 'r') as file:
        data_yaml = yaml.safe_load(file)
    data_yaml['train'] = '../train/images'
    data_yaml['val'] = '../valid/images'
    with open(data_yaml_path, 'w') as file:
        yaml.safe_dump(data_yaml, file)

    class_names = data_yaml['names']
    print("my roboflow classes = ", class_names)
    return dataset_location, data_yaml_path, class_names
