"""Prediction with Machine Learning
"""

from tensorflow import keras
import numpy as np
from typing import List

def predict_images(imgs: List) -> List:
    """Predicts probability of wearing a mask

    Args:
        imgs (List): Detected face image.

    Returns:
        List: Possibly wearing a mask.
    """
    imgs = np.array(imgs)
    model = keras.models.load_model('../models/mask_model.h5')
    preds = model.predict(imgs).tolist()
    return preds

def get_tags(preds: List) -> List:
    """Generate tags for whether or not a mask is worn

    Args:
        preds (List): Possibly wearing a mask.

    Returns:
        List: Tags if you are wearing a mask
    """
    tags = []
    for pred in preds:
        if pred[0]>0.5: tags.append('Without Mask')
        else: tags.append('With Mask')
    return tags