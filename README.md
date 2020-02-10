# ProgImage
The fastest prototyping possible for an upload/download service.

## Specifications
As defined in requirements document

## Challenges
* use streams

## Design principles
* minimize prototyping time
* fastest prototype possible
* Filesystem is assumed to be in the `fs` directory
* No third-party provider
* use Python3.7+

## References
* https://www.starlette.io/requests/#body
* https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
* https://fastapi.tiangolo.com/tutorial/request-files/#define-file-parameters
* https://github.com/tiangolo/fastapi/issues/483
* https://github.com/tiangolo/fastapi/issues/58

## TODOs
* use env variables with docker (debug flags, ...)


## Build
Full build procedure:
````
$ python3.7 -m venv venv
$ source venv/bin/activate
$ $ pip install setuptools --upgrade
$ pip install pip --upgrade
$ pip install -r requirements.txt
$ python src/models.py 
````