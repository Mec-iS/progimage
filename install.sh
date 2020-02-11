python3.7 -m venv venv && \
venv/bin/pip install setuptools --upgrade && \
venv/bin/pip install pip --upgrade && \
venv/bin/pip install -r requirements.txt && \
venv/bin/python src/models.py