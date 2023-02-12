"""API server to determine if a mask is worn or not

API server using FastAPI and implementing mask detection using machine learning.
"""

# Import libraries
from fastapi import FastAPI
import schemas as sh
import json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from machine_learning import preprocessing
from machine_learning import predict
from make_outputdata import make_outputdata

# Create an instance of the application
app = FastAPI()

@app.post('/authentication')
async def authenticate_key(credentials: sh.Credentials) -> dict[str, bool]:
    """Verify that the key sent matches the one you have authorized

    Args:
        credentials (sh.Credentials): [description]

    Returns:
        dict[str, bool]: [description]
    """
    with open('../authentication/secret.json') as f:
        secret: dict[str, str] = json.load(f)
    if credentials.key==secret['KEY']:
        authentication = True
    else:
        authentication = False
    return {'authentication': authentication}

@app.post('/detect_mask', response_model=sh.Pred)
async def detect_mask(input_data: sh.Data) -> sh.Pred:
    """Detect people and determine if they are wearing a mask

    Args:
        input_data (sh.Data): Sent image data.

    Returns:
        sh.Pred: Detection results.
    """
    # Preprocessing
    rectangles = preprocessing.face_detector(input_data.image)
    input_data = preprocessing.crop_images(input_data.image, rectangles)
    # Prediction
    pred_data = predict.predict_images(input_data)
    # Creating response data
    tags = predict.get_tags(pred_data)
    output_data: sh.Pred = make_outputdata(rectangles, tags, pred_data)
    return output_data
