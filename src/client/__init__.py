"""
A client to be used as library to connect to ProgImage storage service
"""
import os
import requests


class ProgImageClient(requests.Session):
    """
    >>> client = ProgImageClient()
    >>> client.post_storage(image='path/filename.jpg')
    >>> # this above returns a unique id (uuid4)
    >>> client.get_storage(id='b1279bac-630e-4335-af0b-0d233550a4d5')
    """
    URL = '127.0.0.1:8000'

    def get_storage(self, **kwargs):
        """
        download image by providing an id
        :param kwargs:
        :return:
        """
        assert 'id' in kwargs.keys(), 'Should specify "id" with unique id value'
        url = f'{self.URL}/storage/{kwargs["id"]}'
        response = super().get(url, **kwargs)
        filename = response.headers['Content-Disposition'].split('filename="')[1]
        with open(filename[0:-1], 'wb+') as f:
            f.write(response.content)

    def post_storage(self, **kwargs):
        assert 'image' in kwargs.keys(), 'Should specify "image" with image path or filename'
        name = os.path.basename(kwargs['image'])
        path_ = kwargs['image']

        url = f'{self.URL}/storage/'
        try:
            files = {'image': (name, open(path_, 'rb'), 'multipart/form-data', {'Expires': '0'})}
        except:
            assert False, 'Cannot find file. Cannot prepare request'

        super().post(url, files=files)
