import torch
import io
from PIL import Image

def get_yolov7():
    model_name = "anpr.pt"
    model = torch.hub.load("./yolov7", 'custom', model_name, source='local')
    return model

def get_image_from_bytes(binary_image, max_size=1024):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = input_image.resize((
        int(input_image.width * resize_factor),
        int(input_image.height * resize_factor)
    ))
    return resized_image