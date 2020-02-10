import pytest
import os
from os.path import join
from starlette.testclient import TestClient

from src import app

from tests import logger, TEST_DATA_DIR

path_ = join(TEST_DATA_DIR, 'test_5mb.jpg')


@pytest.fixture
def client():
    return TestClient(app)


def test_write_multipart(client):
    name = os.path.basename(path_)
    files = {'image': (name, open(path_, 'rb'), 'multipart/form-data', {'Expires': '0'})}
    response = client.post('/storage/', files=files)

    logger.error(response.text)
    assert response.status_code == 200


def test_read_multipart(client):
    name = os.path.basename(path_)
    files = {'image': (name, open(path_, 'rb'), 'multipart/form-data', {'Expires': '0'})}
    response = client.post('/storage/', files=files)

    logger.error(response.text)
    assert response.status_code == 200
