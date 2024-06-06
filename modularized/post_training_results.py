import os
from IPython.display import display, Image

def post_training_results():
    results_dir = os.path.join("runs", "detect", "train")
    best_model_path = os.path.join(results_dir, "weights", "best.pt")
    if os.path.exists(results_dir):
        display(Image(filename=os.path.join(results_dir, "confusion_matrix.png"), width=600))
        display(Image(filename=os.path.join(results_dir, "results.png"), width=600))
        
        print("Trained model files:")
        for file_name in os.listdir(os.path.join(results_dir, "weights")):
            if file_name.endswith(".pt"):
                print(file_name)
    return best_model_path

