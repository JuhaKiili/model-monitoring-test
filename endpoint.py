import json

import random
from werkzeug.debug import DebuggedApplication
from werkzeug.wrappers import Response

predictor = None

def predict_wsgi(environ, start_response):
    from datetime import datetime
    dt = datetime.now()

    print(json.dumps({'vh_metadata': {'confidence': random.random() * 0.5 + 0.1 + dt.second * 0.01}}))
    response = Response(json.dumps({}), mimetype='application/json')
    return response(environ, start_response)


predict_wsgi = DebuggedApplication(predict_wsgi)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 3000, predict_wsgi)
