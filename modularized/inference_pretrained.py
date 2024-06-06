import cv2
import supervision as sv

def inference_pretrained(model, image_path):
    image = cv2.imread(image_path)
    results = model(image)[0]
    detections = sv.Detections.from_ultralytics(results)

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()
    annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)
    sv.plot_image(annotated_image)
