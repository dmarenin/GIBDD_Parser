from flask import Flask
from flask_cors import CORS
import flask_monitoringdashboard as dashboard


app = Flask(__name__)
dashboard.bind(app)
CORS(app, support_credentials=True)

import server.views

