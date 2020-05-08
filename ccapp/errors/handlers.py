from flask import Blueprint, render_template, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return jsonify({'message':'Page Not Found (404), The resource referenced in the URL was not found.'})

@errors.app_errorhandler(403)
def error_403(error):
    return jsonify({'message':'Forbidden (403), The authentication credentials sent with the request are insufficient for the request.'})

@errors.app_errorhandler(500)
def error_500(error):
    return jsonify({'message':'Internal Server Error (500), An unexpected error occurred while processing the request.'})

@errors.app_errorhandler(405)
def error_405(error):
    return jsonify({'message':'Method Not Allowed (405), The method requested is not supported for the given resource.'})

@errors.app_errorhandler(400)
def error_400(error):
    return jsonify({'message':'Bad Request (400), The request is invalid or inconsistent.'})

@errors.app_errorhandler(401)
def error_401(error):
    return jsonify({'message':'Unauthorized (401), The request does not include authentication information or the credentials provided are invalid.'})
