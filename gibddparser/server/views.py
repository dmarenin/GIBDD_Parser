from flask import render_template, request, jsonify
from server import app
import json
import server.exploit as exploit

HEADERS = {"Content-type": "application/json",
           "Access-Control-Allow-Origin": "*", 
           "Access-Control-Expose-Headers": "Access-Control-Allow-Origin",
           "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"}


def result(res, args):
    res = json.dumps(res, default=json_serial)

    return res, 200, HEADERS

def json_serial(obj):
    from datetime import datetime, date
    import decimal
    if isinstance(obj, (datetime, date)):
       return obj.isoformat()

    if isinstance(obj, decimal.Decimal):
       return float(obj)
    pass

@app.errorhandler(KeyError)
def handle_invalid_usage(error):
    str_error = "KeyError: %s" % error

    response = jsonify(str_error)
    response.status_code = 500
    response.content_type = 'text/plain; charset=utf-8'
    
    return response

@app.errorhandler(Exception)
def handle_invalid_usage(error):
    str_error = "Exception: %s" % error

    print(str_error)

    response = jsonify(str_error)
    response.status_code = 500
    response.content_type = 'text/plain; charset=utf-8'
    
    return response

@app.route('/get_info', methods=['GET'])
def get_info():
    args = request.args.to_dict()

    res = exploit.get_data(args)

    return result(res, args)

