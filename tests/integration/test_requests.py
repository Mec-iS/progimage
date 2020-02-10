import unittest
import os
import sys
from os.path import join

import requests

from tests import logger, TEST_DATA_DIR, print_request


class TestExternal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests import stream_handler
        logger.addHandler(stream_handler)
        stream_handler.stream = sys.stdout

        cls.path_ = join(TEST_DATA_DIR, 'test_5mb.jpg')

    def setUp(self):
        self.f_descriptor = open(self.path_, 'rb')
        self.session = requests.Session()

    def test_post_get_file_form_data(self):
        name = os.path.basename(self.path_)
        files = {'image': (name, self.f_descriptor, 'multipart/form-data', {'Expires': '0'})}

        req = requests.Request(
            method='POST',
            url='http://localhost:8000/storage/',
            files=files,
        )
        prepared = req.prepare()
        print_request(logger, prepared)
        response = self.session.send(prepared)

        assert response.status_code == 200

        json = response.json()
        logger.debug(json)

        req = requests.Request(
            method='GET',
            url=f'http://localhost:8000/storage/{json["id"]}',
        )

        prepared = req.prepare()
        print_request(logger, prepared)
        response = self.session.send(prepared)

        logger.debug(response.status_code)
        assert response.status_code == 200

    def test_post_image_jpg(self):
        name = os.path.basename(self.path_)
        files = {'image': (name, self.f_descriptor, 'image/jpg', {'Expires': '0'})}

        req = requests.Request(
            method='POST',
            url='http://localhost:8000/storage/',
            files=files,
        )
        prepared = req.prepare()
        print_request(logger, prepared)
        response = self.session.send(prepared)
        logger.debug(response.json())

    def tearDown(self):
        self.session.close()
        self.f_descriptor.close()

    @classmethod
    def tearDownClass(cls):
        from tests import stream_handler
        logger.removeHandler(stream_handler)
