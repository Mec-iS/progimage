"""
ProgImage: a programmatic API to store and process images
"""
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount

# import handlers
import src.storage as storage
import src.converter as converter

from src.config import FS_DIR

routes = [
    Mount('/storage', routes=[
        Route('/', endpoint=storage.post, methods=['POST']),
        Route('/{id_}', endpoint=storage.get, methods=['GET']),
    ]),
    Mount('/converter', routes=[
        Route('/{id_}/{format}', endpoint=converter.format, methods=['GET']),
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

