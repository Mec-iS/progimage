from starlette.responses import JSONResponse


def error_response(msg, code):
    return JSONResponse(content={'message': msg, 'code': str(code)},
                        status_code=code)




