"""
Module: directories
"""
import os


class Directories:
    """
    For clearing & creating directories
    """

    def __init__(self):
        """

        """

    @staticmethod
    def cleanup(path: str):
        """
        Clears a directory

        :param path:
        :return:
        """

        # Foremost, delete files
        files_ = [os.remove(os.path.join(base, file))
                  for base, _, files in os.walk(path) for file in files]

        if any(files_):
            raise Exception(f'Unable to delete all files within path {path}')

        # ... then, directories
        directories_ = [os.removedirs(os.path.join(base, directory))
                        for base, directories, _ in os.walk(path, topdown=False)
                        for directory in directories
                        if os.path.exists(os.path.join(base, directory))]

        if any(directories_):
            raise Exception(f'Unable to delete all directories within path {path}')

    @staticmethod
    def create(path: str):
        """

        :param path:
        :return:
        """

        if not os.path.exists(path):
            os.makedirs(path)
