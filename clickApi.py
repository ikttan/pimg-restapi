#!/usr/bin/python

from flask import Flask, request, Response
import time
import jsonpickle
import base64
import cv2

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method, you can use others as well, but make sure that this is reflected corrected on the Raspberry Pi side, the click.py file from above.
@app.route('/api/click', methods=['POST'])

def test():
    r = request
    # setfile name based on time, which is a floating point but we only need it to the integer
    rfile = str(int(time.time())) + ".jpg"
    # decode image
    img  = base64.b64decode(r.data)
    with open(rfile, 'wb') as f:
        f.write(img)

    # probably a better way to do this without OpenCV
    myImg = cv2.imread(rfile)
    response = {'message': 'image received. size= %d x %d' % (myImg.shape[1], myImg.shape[0] )}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
# host="0.0.0.0" allows it to be accessed from external IP
app.run(host="0.0.0.0", port=5000)
