from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount

from src.handlers import storage
from src.config import FS_DIR

routes = [
    Mount('/storage', routes=[
        Route('/', endpoint=storage, methods=['POST']),
        Route('/{id_}', endpoint=storage, methods=['GET']),
    ])
]

app = Starlette(debug=True, routes=routes)
app.mount('/fs', StaticFiles(directory='fs'), name='fs')


@app.exception_handler(404)
async def not_found(request, exc):
    """
    Custom 404
    """
    return JSONResponse({'error': True, 'code': '404', 'msg': str(exc)})


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Custom 505
    """
    return JSONResponse({'error': True, 'code': '500', 'msg': str(exc)})

