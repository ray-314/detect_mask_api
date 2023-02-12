"""Preprocessing for machine learning to predict
"""

import cv2, dlib
import numpy as np
from typing import List

def face_detector(img: List) -> List[List[int]]:
    """AI is creating summary for face_detector

    Args:
        img (List): Input image.

    Returns:
        List[List[int]]: Data on face position.
    """
    rectangles = []
    detector = dlib.get_frontal_face_detector()
    img = np.array(img, dtype = 'uint8')
    dets = detector(img, 1)
    for d in dets:
        x1, y1, x2, y2 = int(d.left()), int(d.top()), int(d.right()), int(d.bottom())
        rectangles.append([x1, y1, x2, y2])
    return rectangles

def crop_images(img: List, rectangles: List) -> List:
    """Extract faces from images using facial location data

    Args:
        img (List): Input image.
        rectangles (List): Data on face position.

    Returns:
        List: Extracted face image data.
    """
    imgs = []
    img = np.array(img, dtype = 'uint8')
    for rectangle in rectangles:
        detect_face = img[rectangle[1]:rectangle[3], rectangle[0]:rectangle[2]]
        # Process to adjust the image size to 50 x 50, which is the image size for learning.
        try:
            detect_face = cv2.resize(detect_face, (50,50))
        except:
            pass
        detect_face = cv2.cvtColor(detect_face, cv2.COLOR_RGB2BGR)
        imgs.append(detect_face)
    return imgs