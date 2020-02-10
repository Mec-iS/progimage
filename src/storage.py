"""
As set of handlers to deploy a simple storage for files

* POST method: upload
* GET method: download
"""
import os
import uuid

from starlette.responses import JSONResponse
from aiofile import AIOFile

from src.utils import error_response
from src.config import FS_DIR

from src.config import logger


async def get(request):
    """
    Implement GET for download.
    :param request: (starlette.requests.Request)
    :return: (starlette.Response.FileResponse)
    """
    # retrieve unique id
    uuid_ = request.path_params['id_']

    # retrieve record
    from src.models import select_from_index
    cursor = select_from_index(uuid_)
    count = 0
    name = None
    for r in cursor:
        logger.debug(r)
        id_, name, uuid_ = r
        count += 1
        break
    if count != 1: return error_response('Wrong unique id', 404)

    # parse file data
    filename = f'{uuid_}_{name}'
    path_ = os.path.join(FS_DIR, filename)
    ext = name.split('.')[1]

    from starlette.responses import FileResponse
    return FileResponse(path_, media_type=f"image/{ext}", filename=filename)


async def post(request):
    """
    Implement POST for upload.
    :param request: (starlette.requests.Request)
    :return: (starlette.Response.JSONResponse)
    """
    form = await request.form()
    logger.debug(form)
    uuid_ = str(uuid.uuid4())
    filename = f'{uuid_}_{form["image"].filename}'
    path_ = os.path.join(FS_DIR, filename)

    from src.models import insert_to_index
    insert_to_index(form["image"].filename, uuid_)

    async with AIOFile(path_, 'ab+') as afp:
        contents = await form["image"].read()
        await afp.write(contents)
        await afp.fsync()

    return JSONResponse(
        {'message': 'file created, uploading started', 'id': uuid_,
         'full_name': filename,
         'content_type': request.headers['content-type']})
