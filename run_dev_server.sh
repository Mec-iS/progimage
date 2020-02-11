#
# uvicorn is a minimal low-level server/application interface for asyncio frameworks
#
venv/bin/uvicorn src:app

#
# Gunicorn is a mature, fully featured server and process manager.
#
## This allows you to increase or decrease the number of worker processes on the fly,
## restart worker processes gracefully, or perform server upgrades without downtime.
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker --log-level debug src:app