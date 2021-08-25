import torch

# Load model
model = torch.hub.load(
    repo_or_dir='ultralytics/yolov5',
    model='yolov5s',
    pretrained=True,
    # force_reload=True
)

imgs = ['https://ultralytics.com/images/zidane.jpg']

# Detect image from pre-trained model
results = model(imgs)

# Print Results
results.print()

