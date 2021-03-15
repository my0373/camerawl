from pathlib import Path
from os import listdir
from os.path import isfile, join
import os
# TODO: Tidy up the imports


class ImageRepo:
    """
    The ImageRepo class is a collection of ImagePaths to scan
    """

    def __init__(self, *paths):
        """

        :type paths: object
        """
        # _paths is an internal list of
        self._paths = paths

    def scan(self):
        """
        Scan the ImagePaths
        :return: tuple of files.
        """
        self._files = []

        # Loop through the paths scanning them all and adding all the
        # files to a list.

        # Check that there is actually a path to scan. We also want to
        # make sure that if the paths have no files or directories, we
        # just return None.
        # TODO: Probably want to raise and handle a nice exception here.
        if self._paths:
            for _path in self._paths:
                _filelist = _path.scan()
                if _filelist:
                    for _file in _filelist:
                        if isfile(_file):
                            self._files.append(_file)

            # We return a Tuple because they are immutable.
            # Immutable data structures make me happy as they CANNOT
            # be changed by some misbehaving code :)
            #
            # If we don't have anything to return then just return an empty Tuple.
            return tuple(self._files)
        else:
            return ()


class ImagePath:
    """
    A path representing a path that stores images.

    """

    def __init__(self, path):
        self._path = path
        self._files = []

    def scan(self):
        """
        Scan the path and return the results
        :return:
        """
        self._files = []



        # TODO: Write some working scan code.
        if self._scandirs():
            self._files = self._scandirs()
            return tuple(self._files)
        else:
            return None

    def _scandirs(self):
        for root, dirs, files in os.walk(self._path, topdown=False):
            for name in files:
                print(os.path.join(root, name))


    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def __str__(self):
        return self._path

