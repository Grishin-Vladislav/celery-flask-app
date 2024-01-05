import base64

import requests
from flask import Flask, jsonify, request
from flask.views import MethodView
from werkzeug.utils import secure_filename

from upscaler.upscale import upscale

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def is_allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UpscaleView(MethodView):
    def post(self):
        for img in request.files.values():
            if not is_allowed_file(img.filename):
                return jsonify({'error': 'File type not allowed'}), 400
            name = secure_filename(img.filename)
            print(name)
        #     image = img.stream.read()

        # with open('copy.png', 'wb') as f:
        #     f.write(base64.b64decode(image))

        return jsonify({'hello': 'world'}), 200


upscale_view = UpscaleView.as_view('upscale_view')

app.add_url_rule('/upscale', view_func=upscale_view, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
