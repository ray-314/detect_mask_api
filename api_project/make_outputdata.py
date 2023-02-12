"""Creation of output data
"""

import schemas as sh
from typing import List

def make_outputdata(rectangles: List, tags: List, preds: List) -> sh.Pred:
    """Summarize and format data into output data

    Args:
        rectangles (List): Rectangle data by face detection.
        tags (List): Tag with or without mask.
        preds (List): Prediction Results.

    Returns:
        sh.Pred: Output data generated.
    """
    output_data = {
        'rectangles': [],
        'tags': tags,
        'confidence': []
    }
    for rectangle in rectangles:
        rectangle_dict = {
            'top':rectangle[1],
            'bottom':rectangle[3],
            'left':rectangle[0],
            'right':rectangle[2]
        }
        output_data['rectangles'].append(rectangle_dict)
    for pred in preds:
        confidence_dict = {
            'without_mask': pred[0],
            'with_mask': pred[1]
        }
        output_data['confidence'].append(confidence_dict)
    return output_data