from flask import make_response


def empty_response(code):
    response = make_response('', code)
    return response
