from marshmallow import ValidationError
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import InvalidRequestError


def register_error_handlers(app):
    app.register_error_handler(ValidationError, schema_validation_error)
    app.register_error_handler(NotFound, not_found_error)
    app.register_error_handler(InvalidRequestError, invalid_request_error)
    app.register_error_handler(Exception, server_error)

def schema_validation_error(err):
    return {"message": err.messages}, 400

def invalid_request_error(err):
    return {"message": "Unable to complete request, payload and/or query params may be invalid."}, 400

def not_found_error(err):
    return {"message": "Sorry the resource was not found."}, 404

def server_error(err):
    return {"message": "Sorry our server had an error, we are looking into it!"}, 500
