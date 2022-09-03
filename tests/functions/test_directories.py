import os

import pytest

import src.functions.directories


class TestDirectories:

    @pytest.fixture()
    def directories(self):
        return src.functions.directories.Directories()

    @pytest.fixture()
    def path(self):
        return os.path.join(os.getcwd(), 'warehouse', 'tests')

    def test_create(self, directories, path):
        directories.create(path=path)
        assert os.path.exists(path=path)

    def test_cleanup(self, directories, path):
        directories.cleanup(path=path)
        assert not os.path.exists(path=path)
