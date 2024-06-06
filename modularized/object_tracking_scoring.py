import os
import cv2
import supervision as sv
from ultralytics import YOLOv10
import numpy as np

def object_tracking_scoring(video_path, best_model_path):
    # Load the best trained model
    trained_model = YOLOv10(best_model_path)
    
    # Initialize trackers and annotators
    tracker = sv.ByteTrack()
    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()
    trace_annotator = sv.TraceAnnotator()

    # Initialize score and intersection tracking
    score = 0
    intersected_basketballs = set()

    # Function to check intersection
    def check_intersection(basketball_box, hoop_box):
        x1_b, y1_b, x2_b, y2_b = basketball_box
        x1_h, y1_h, x2_h, y2_h = hoop_box
        
        # Check if the boxes intersect
        if x1_b < x2_h and x2_b > x1_h and y1_b < y2_h and y2_b > y1_h:
            return True
        return False

    # Callback function for processing each frame
    def callback(frame: np.ndarray, _: int) -> np.ndarray:
        nonlocal score, intersected_basketballs
        results = trained_model(frame)
        print("Results type:", type(results))
        print("Results:", results)
        
        # Extract results from the list
        results = results[0]
        
        # Convert the results to Detections
        detections = sv.Detections.from_ultralytics(results)
        
        # Update detections with tracker
        detections = tracker.update_with_detections(detections)
        
        # Generate labels
        labels = [
            f"#{tracker_id} {trained_model.names[class_id]}"
            for class_id, tracker_id in zip(detections.class_id, detections.tracker_id)
        ]
        
        # Ensure that labels list matches the number of detections
        if len(labels) != len(detections):
            print(f"Warning: Number of labels ({len(labels)}) does not match number of detections ({len(detections)})")
            return frame  # Return the original frame if there's a mismatch

        # Get bounding boxes and tracker IDs for basketball and hoop
        basketball_boxes = [(box, tracker_id) for box, class_id, tracker_id in zip(detections.xyxy, detections.class_id, detections.tracker_id) if class_id == 1]
        hoop_boxes = [(box, tracker_id) for box, class_id, tracker_id in zip(detections.xyxy, detections.class_id, detections.tracker_id) if class_id == 2]
        
        # Check for intersection and update score
        for basketball_box, basketball_id in basketball_boxes:
            for hoop_box, hoop_id in hoop_boxes:
                if check_intersection(basketball_box, hoop_box):
                    if basketball_id not in intersected_basketballs:
                        score += 1
                        intersected_basketballs.add(basketball_id)

        # Annotate frame with bounding boxes and labels
        annotated_frame = bounding_box_annotator.annotate(frame.copy(), detections=detections)
        annotated_frame = label_annotator.annotate(annotated_frame, detections=detections, labels=labels)

        # Overlay the score on the frame
        cv2.putText(annotated_frame, f"Score: {score}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        
        return trace_annotator.annotate(annotated_frame, detections=detections)

    # Process video with tracking and scoring using the updated callback
    sv.process_video(source_path=video_path, target_path=os.path.join("result.mp4"), callback=callback)
