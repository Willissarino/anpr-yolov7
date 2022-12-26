import io
import json
import base64
from config import get_yolov7, get_image_from_bytes
from fastapi import FastAPI, File
from starlette.responses import Response
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

model = get_yolov7()

app = FastAPI(
    title="Custom YOLOV7 Machine Learning API",
    description="""Obtain object value out of image
    and return image and json result""",
    version="1",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

@app.post("/object-to-json")
async def detect_img_return_json_result(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image)
    results.render()  # updates results.imgs with boxes and labels
    detect_res = results.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)
    for img in results.imgs:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(bytes_io, format="jpeg")
    return {"result": detect_res}

@app.post("/object-to-img")
async def detect_img_return_base64_img(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image)
    results.render()  # updates results.imgs with boxes and labels
    for img in results.imgs:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(bytes_io, format="jpeg")
    return Response(content=bytes_io.getvalue(), media_type="image/jpeg")
