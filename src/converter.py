"""
A set of handlers to deploy operations on images files

example of image transformations in OpenCV:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
"""
from starlette.responses import JSONResponse


async def format(request):
    """Convert an image to another format
    """
    pass


async def example_resize(request):
    """Use an exemplary resize function.
    Leveraging Rust image library <https://github.com/image-rs/image/blob/master/examples/scaleup>
    """
    from cffi import FFI
    ffi = FFI()
    ffi.cdef('int rs_resize(const char *);')

    lib = ffi.dlopen('./imgproc/target/release/deps/libc_rs_imgproc.dylib')

    try:
        lib.rs_resize('some/path_to_image')
        return JSONResponse({'message': 'Resize completed. See files in fs'})
    except:
        return JSONResponse({'message': 'Error in rs_resize'})

