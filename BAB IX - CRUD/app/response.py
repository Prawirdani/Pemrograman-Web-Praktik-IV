from flask import jsonify, make_response

def OK(values, message):
    res = {
        "values":values,
        "message":message
    }
    return make_response(jsonify(res), 200) 

def NOT_FOUND(values, message):
    res = {
        "values":values,
        "message":message
    }
    return make_response(jsonify(res), 404) 

def BAD_REQUEST(values, message):
    res = {
        "values":values,
        "message":message
    }
    return make_response(jsonify(res), 400) 