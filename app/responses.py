from flask import jsonify

def bad_request(message='Bad request'):
    return jsonify(
        {
            "success": False,
            "message": message,
            "error_code": 404,
            "data": {}
        }
    ), 400

def not_found(message='Resource doesn`t not exists'):
    return jsonify(
        {
            "success": False,
            "message": message,
            "error_code": 404,
            "data": {}
        }
    ), 404

def response(data, code=200):
    return jsonify(
        {
            "success": True,
            "data": data
        }
    ), code
