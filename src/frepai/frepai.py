import re


class Frepai:
    """
    Frepai - File replication and inspection class
    """

    def __init__(self):
        """
        Constructor
        """
        self.basedir = None
        self.pattern = None

        pass

    def index(self, basedir=None, pattern=''):
        """
        Walk the filesystem of a base directrory and get a list of files present.


        basedir - string - the Path to start searching
        pattern - Python Regex pattern to be applied to all filenames in the tree. Any files not matching this pattern will be discarded.


        :return:
        """

        # Set attributes for the search.
        self.basedir = re.compile(basedir)
        self.pattern = pattern

        # TODO: We need to return a value with a list of all the files, or callback to an interator or something. To be figured out when I'm not half asleep.



