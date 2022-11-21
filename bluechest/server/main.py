import io 
import shutil 

from fastapi import FastAPI, UploadFile, File
from PIL import Image


from libs.base.base_predictor import BasePredictor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # with open(f'{file.filename}', 'wb') as buffer:
    # shutil.copyfileobj(file.file, buffer)
    default_size = (224, 224)
    contents = await file.read()
    pil_image = Image.open(io.BytesIO(contents))
    pil_image = pil_image.resize(default_size)

    # scope
    scope = "breast_cancer"
    # instanciate base predictor
    base_predictor = BasePredictor(scope=scope)
    results = base_predictor.predict(image=pil_image)

    return results

