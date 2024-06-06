import argparse
from modularized.setup_and_installation import setup_and_install
from modularized.download_weights import download_weights
from modularized.initialize_model import initialize_model
from modularized.download_dataset import download_dataset
from modularized.inference_pretrained import inference_pretrained
from modularized.custom_training import custom_training
from modularized.post_training_results import post_training_results
from modularized.download_video import download_video
from modularized.object_tracking_scoring import object_tracking_scoring

def main(args):
    # Setup and Installation
    setup_and_install()
    
    # Download YOLOv10 Weights
    download_weights()
    
    # Initialize YOLOv10 Model
    weights_dir = "weights"
    model, device = initialize_model(weights_dir)
    
    # Download Dataset from Roboflow
    dataset_location, data_yaml_path, class_names = download_dataset()
    
    # Inference with Pre-trained Model
    inference_pretrained(model, args.image_path)
    
    # Custom Training
    custom_training(weights_dir, data_yaml_path, device, args.epochs, args.batch_size)
    
    # Post-training Results and Visualization
    best_model_path = post_training_results()
    
    # Download High-Quality Video from YouTube
    video_path = download_video(args.yt_video_url)
    
    # Object Tracking and Scoring
    object_tracking_scoring(video_path, best_model_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv10 Training and Inference Pipeline")
    parser.add_argument("--epochs", type=int, default=25, help="Number of epochs for training")
    parser.add_argument("--batch_size", type=int, default=8, help="Batch size for training")
    parser.add_argument("--image_path", type=str, default="your_image.png", help="Path to the image for inference")
    parser.add_argument("--yt_video_url", type=str, default="https://www.youtube.com/watch?v=KyC6wr4I2VU", help="URL of the YouTube video for object tracking and scoring")
    args = parser.parse_args()
    main(args)

