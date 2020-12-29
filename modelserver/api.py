import flask
import json
from flask import request, jsonify

import tensorflow.compat.v1 as tf
import tensorflow_hub as hub

from models import USE_lite


tf.disable_v2_behavior()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

global Model, graph
Model = USE_lite()
# graph = tf.Graph()
Model.load_persisting_model()


@app.route('/embeddings', methods=['POST'])
def home():
    request_data = json.loads(request.data)
    messages = request_data.get('data')

    embeddings, corr = Model.get_embeddings_and_corr(messages)
    embeddings = embeddings.tolist()
    corr = corr.tolist()

    return jsonify(corr) 


def model_status():
    if Model.module and Model.graph and Model.encodings:
        response = {
            'status': 'READY'
        }
    else:
        response = {
            'status': 'NOT READY'
        }
    return response


if __name__ == '__main__':   
    app.run(threaded=True)

