import os
import uuid

from starlette.responses import JSONResponse, StreamingResponse

from src.utils import error_response
from src.config import FS_DIR

from src.config import logger

from aiofile import AIOFile


async def storage(request):
    # TODO: create mapping method-function
    # TODO: check content-type, read file extension <- check_content_type()
    if request.method == 'GET':
        uuid_ = request.path_params['id_']
        logger.info(uuid_)
        #return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

    if request.method == 'POST':
        form = await request.form()
        id_ = str(uuid.uuid4())
        filename = f'{id_}_{form["image"].filename}'
        path_ = os.path.join(FS_DIR, filename)

        async with AIOFile(path_, 'ab+') as afp:
            contents = await form["image"].read()
            await afp.write(contents)
            await afp.fsync()

        return JSONResponse(
            {'message': 'file created, uploading started', 'id': id_,
             'full_name': filename,
             'content_type': request.headers['content-type']})
    else:
        return JSONResponse({'msg': None}), 500
