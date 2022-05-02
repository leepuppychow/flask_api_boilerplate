def register_error_handlers(app):
    """
    Can register error handlers for specific exceptions or status codes,
    and then pass them to a handler function:
    
    https://flask.palletsprojects.com/en/2.1.x/errorhandling/
    """
    # app.register_error_handler(Exception, server_error)


def server_error(err):
    return {"message": "Sorry our server had an error, we are looking into it!"}, 500
