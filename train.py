from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from YAML
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data=r'ultralytics/cfg/datasets/signature.yaml',
                      epochs=100,
                      imgsz=640,
                      project=r'path/to/your/project',
                      name='signature_tracker_model')
