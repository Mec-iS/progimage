# ProgImage
A mini-project to demonstrate a fast-prototyping workflow for an image repository/processing service.

This mini-project is based on [Python coroutines (also known as async/await protocol or simply `asyncio`)](https://docs.python.org/3/library/asyncio.html).
 It leverages ASGI (Asynchronous Gateway Interface via `uvicorn`) that is the step forward from uWSGI to a
 concurrent server implementation. The framework used is [Starlette](https://www.starlette.io/), an
 async-native Flask-inspired library to create highly concurrent applications.  

## Specifications
As defined in requirements document

## Architecture
The basic implementation is the work of three basic architectural modules: 

A. a web server

B. a key-value store

C. a file system

The tools/libraries used to implement these modules have been picked considering a trade-off in
 terms of time-effectiveness of the implementation and fitness to the requested operations.
 According to the [design principles](#design-principles) defined at the beginning of the task, the
 tools chosen, and relative motivations, have been:

A. Starlette and Gunicorn: ASGI-native, functional style, fast, multi-process manager;

B. sqlite: easy to deploy, relatively-fast SQL for average scale. a NoSQL or a cache would be fitter;

C. a POSIX file system: the codebase uses Async File I/O on a regular filesystem, a third party
    cloud storage can be easily plugged-in.

## Design principles
* minimized prototyping time (not more than 10 hours)
* fastest prototype possible
* Filesystem is assumed to be in a `fs` directory that can be easily moved to a Docker volume
* Database is assumed to be in a `db` directory that can be easily moved to a Docker volume
* No third-party provider
* use Python3.7+

## Challenges
* use asynchronous programming
* maintain high modularity and extensibility of the API
* squeeze over-the-par performance from Python
* time constraint
* develop a client library (`ProgImageClient`) in few lines of code

## References
* [Request object in Starlette](https://www.starlette.io/requests/#body)
* [File handling in FastAPI](https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile)

## TODOs
* use env variables with docker (debug flags, ...)
* implement storing size of the files in key-value
* move to `async_pg` or other aync driver as `sqlite3` has no native async support
* add `docker-compose` with multi-volume support 


## Build
Full build procedure:
````
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install setuptools --upgrade
$ pip install pip --upgrade
$ pip install -r requirements.txt
$ python src/models.py
$ ./run.sh
````

## Testing
After building is possible to run unit tests or integration tests against the local server.

### unit test with pytest
```
$ pytest tests/unit
```

### integration tests
With a local instance running
```
$ python -m unittest tests.integration.test_requests.TestExternal
```

