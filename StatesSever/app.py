import os 
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
from StatesSever.swagger_config import swagger_config
from StatesSever.swagger_template import swagger_template

app = Flask(__name__)
CORS(app)
swagger = Swagger(app, config=swagger_config, template=swagger_template)

@app.route('/', methods=['GET'])
@swag_from('swaggerDocs/home.yml')
def home():
    return jsonify({"mensaje": "Hello world!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)