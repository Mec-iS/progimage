from starlette.responses import JSONResponse


def error_response(msg, code):
    return JSONResponse({'message': msg, 'code': str(code)})


