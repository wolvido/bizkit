import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200

# def is_match(fave_numbers_1, fave_numbers_2):
#     for number in fave_numbers_2:
#         if number not in fave_numbers_1:
#             return False

#     return True

def is_match(arr2,arr1):
    arr1Sort = sorted(arr1)
    arr2Sort = sorted(arr2)
    shiftCounter = 0
    counter = 0

    for i in arr1Sort:
        while True:
            if shiftCounter > len(arr2) and i != arr2Sort[shiftCounter]:
                return False
            elif i < arr2Sort[shiftCounter]:
                return False                
            elif i != arr2Sort[shiftCounter] and i > arr2Sort[shiftCounter]:
                shiftCounter += 1
            else:
                shiftCounter += 1
                counter += 1
                break
        if counter == (len(arr1)):
            return True
