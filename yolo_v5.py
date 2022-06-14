import io
import torch
from PIL import Image



def predict_object_detection(file_name):
    file_path="static\\uploads\\"+file_name
    model = torch.hub.load('ultralytics/yolov5', 'custom', path="static/Model/Yolov5.pt", force_reload=True)
    model.eval()
    with open(file_path, "rb") as image:
        f = image.read()
        b = bytearray(f)
        img = Image.open(io.BytesIO(b))
        img.thumbnail((416, 416), Image.Resampling(1))
        results = model(img, size=416)
        # for debugging
        # data = results.pandas().xyxy[0].to_json(orient="records")
        # return data

        results.render()  # updates results.imgs with boxes and labels
        for img in results.imgs:
            img_base64 = Image.fromarray(img)
            img_base64.save(file_path+"detected.jpeg", format="JPEG")
    return file_name+"detected.jpeg"

